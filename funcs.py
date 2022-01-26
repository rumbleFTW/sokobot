def printf(obj):
    for i in range(0, len(obj.matrix)):
        for j in range(0, len(obj.matrix[0])):
            if(i == obj.playerY and j == obj.playerX):
                print("@", end = '')
            else:
                print(obj.matrix[i][j], end = '')
        print()
    print("")

def check(currLevel):
    clear = True
    for i in range(0, currLevel.rows):
        for j in range(0, currLevel.cols):
            if currLevel.matrix[i][j] == 2:
                clear = False
    return clear
 
def move(currLevel, vals):
    if currLevel.matrix[currLevel.playerY+vals[1]][currLevel.playerX+vals[0]] == 0 or currLevel.matrix[currLevel.playerY+vals[1]][currLevel.playerX+vals[0]] == 2:
        currLevel.playerY += vals[1]
        currLevel.playerX += vals[0]
        currLevel.timeLine.append(vals)
    else:
        currLevel.matrix[currLevel.playerY+vals[1]][currLevel.playerX+vals[0]] -= 3
        currLevel.matrix[currLevel.playerY+2*vals[1]][currLevel.playerX+2*vals[0]] += 3
        currLevel.playerY += vals[1]
        currLevel.playerX += vals[0]
        currLevel.timeLine.append(vals)

def isLegal(currLevel, vals):
    if currLevel.matrix[currLevel.playerY+vals[1]][currLevel.playerX+vals[0]] == 1:
        return False
    elif currLevel.matrix[currLevel.playerY+vals[1]][currLevel.playerX+vals[0]] == 2 or currLevel.matrix[currLevel.playerY+vals[1]][currLevel.playerX+vals[0]] == 0:
        return True
    elif  currLevel.matrix[currLevel.playerY+2*vals[1]][currLevel.playerX+2*vals[0]] != 1 and currLevel.matrix[currLevel.playerY+2*vals[1]][currLevel.playerX+2*vals[0]] < 3:
        return True
    return False

def blocked(currLevel, vals):
    if currLevel.matrix[currLevel.playerY+vals[1]][currLevel.playerX+vals[0]] == 3 and currLevel.matrix[currLevel.playerY+2*vals[1]][currLevel.playerX+2*vals[0]] != 2:
        if(currLevel.matrix[currLevel.playerY+2*vals[1]+1][currLevel.playerX+2*vals[0]] == 1 and currLevel.matrix[currLevel.playerY+2*vals[1]][currLevel.playerX+2*vals[0]+1] == 1):
            return True
        elif(currLevel.matrix[currLevel.playerY+2*vals[1]+1][currLevel.playerX+2*vals[0]] == 1 and currLevel.matrix[currLevel.playerY+2*vals[1]][currLevel.playerX+2*vals[0]-1] == 1):
            return True    
        elif(currLevel.matrix[currLevel.playerY+2*vals[1]-1][currLevel.playerX+2*vals[0]] == 1 and currLevel.matrix[currLevel.playerY+2*vals[1]][currLevel.playerX+2*vals[0]+1] == 1):
            return True   
        elif(currLevel.matrix[currLevel.playerY+2*vals[1]-1][currLevel.playerX+2*vals[0]] == 1 and currLevel.matrix[currLevel.playerY+2*vals[1]][currLevel.playerX+2*vals[0]-1] == 1):
            return True  
    return False

def searchHist(gameState, hist):
    for item in hist:
        if item.matrix == gameState.matrix:
            if(item.playerY == gameState.playerY and item.playerX == gameState.playerX):
                return True
    return False

def moveDictation(moves):
    moveNames = {(1, 0): "Right", (-1, 0): "Left", (0, 1): "Down", (0, -1): "Up"}
    for item in moves:
        print(moveNames[item], end = "=>")

def wallFreeFaces(matrix, pos):
    res = []
    if pos[0] > 0 and matrix[pos[0]-1][pos[1]] not in (1, 6):
        res.append((-1, 0))
    if pos[0] < len(matrix)-1 and (matrix[pos[0]+1][pos[1]]) not in (1, 6):
        res.append((1, 0))
    if pos[1] > 0 and matrix[pos[0]][pos[1]-1] not in (1, 6):
        res.append((0, -1))
    if pos[1] < len(matrix[0])-1 and matrix[pos[0]][pos[1]+1] not in (1, 6):
        res.append((0, 1))
    return res

def manhattanDist(gameState, boxPos):                               #Manhattan distances between all the possible 
    dist = []                                                       #destinations and the current box
    for i in range(0, gameState.rows):
        for j in range(0, gameState.cols):
            if gameState.matrix[i][j] == 2:
                dist.append(abs(boxPos[0]-i)+abs(boxPos[1]-j))
    return dist

