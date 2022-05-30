from threading import Thread
import os
import pygame
import copy
from levels import *
from funcs import *
from depthFirstSearch import *
from breadthFirstSearch import *
from aStarManhattan import *


APP_FOLDER = os.path.dirname( os.path.realpath( __file__ ) )+os.path.sep+'assets'

levels = [l1, l2, l3, l4, l5, l6]
levelIndex = 0
currLevel = copy.deepcopy(levels[levelIndex])

icon = pygame.image.load(os.path.join(APP_FOLDER, "icon.png"))
aStarBtn = pygame.image.load(os.path.join(APP_FOLDER, "aStarBtn.png"))
bfsBtn = pygame.image.load(os.path.join(APP_FOLDER, "bfsBtn.png"))
dfsBtn = pygame.image.load(os.path.join(APP_FOLDER, "dfsBtn.png"))

crate = pygame.image.load(os.path.join(APP_FOLDER, "crate.png"))
treasure = pygame.image.load(os.path.join(APP_FOLDER, "treasure.png"))

wb = pygame.image.load(os.path.join(APP_FOLDER, "wb.png"))
wl = pygame.image.load(os.path.join(APP_FOLDER, "wl.png"))
wr = pygame.image.load(os.path.join(APP_FOLDER, "wr.png"))
wt = pygame.image.load(os.path.join(APP_FOLDER, "wt.png"))
wb = pygame.image.load(os.path.join(APP_FOLDER, "wb.png"))
wlt = pygame.image.load(os.path.join(APP_FOLDER, "wlt.png"))
wlb = pygame.image.load(os.path.join(APP_FOLDER, "wlb.png"))
wrt = pygame.image.load(os.path.join(APP_FOLDER, "wrt.png"))
wrb = pygame.image.load(os.path.join(APP_FOLDER, "wrb.png"))

wtb = pygame.image.load(os.path.join(APP_FOLDER, "wtb.png"))
wlr = pygame.image.load(os.path.join(APP_FOLDER, "wlr.png"))
w3l = pygame.image.load(os.path.join(APP_FOLDER, "w3l.png"))
w3r = pygame.image.load(os.path.join(APP_FOLDER, "w3r.png"))
w3t = pygame.image.load(os.path.join(APP_FOLDER, "w3t.png"))
w3b = pygame.image.load(os.path.join(APP_FOLDER, "w3b.png"))
w4 = pygame.image.load(os.path.join(APP_FOLDER, "w4.png"))
charS = pygame.image.load(os.path.join(APP_FOLDER, "charS.png"))

tl = (pygame.image.load(os.path.join(APP_FOLDER, "tl1.png")),pygame.image.load(os.path.join(APP_FOLDER, "tl2.png")))
td = (pygame.image.load(os.path.join(APP_FOLDER, "td1.png")),pygame.image.load(os.path.join(APP_FOLDER, "td2.png")))
tls =(pygame.image.load(os.path.join(APP_FOLDER, "tls1.png")),pygame.image.load(os.path.join(APP_FOLDER, "tls2.png")))
tds = (pygame.image.load(os.path.join(APP_FOLDER, "tds1.png")),pygame.image.load(os.path.join(APP_FOLDER, "tds2.png")))
coin = (pygame.image.load(os.path.join(APP_FOLDER, "c1.png")), pygame.image.load(os.path.join(APP_FOLDER, "c2.png")), pygame.image.load(os.path.join(APP_FOLDER, "c3.png")), pygame.image.load(os.path.join(APP_FOLDER, "c4.png")), pygame.image.load(os.path.join(APP_FOLDER, "c5.png")), pygame.image.load(os.path.join(APP_FOLDER, "c6.png")), pygame.image.load(os.path.join(APP_FOLDER, "c7.png")), pygame.image.load(os.path.join(APP_FOLDER, "c8.png")))
char = (pygame.image.load(os.path.join(APP_FOLDER, "char1.png")), pygame.image.load(os.path.join(APP_FOLDER, "char2.png")))
animPtr = 0

clock = pygame.time.Clock()

def render(currLevel, screen):
    x = (416-32*currLevel.rows)//2
    for i in range(0, currLevel.rows):
        y = (416-32*currLevel.cols)//2
        for j in range(0, currLevel.cols):
            if currLevel.matrix[i][j]  == 1:
                wallType = wallFreeFaces(currLevel.matrix, (i, j))
                if len(wallType) == 1:
                    if(i+j)%2 == 0:
                        screen.blit(td[(i*j)%2], (y, x))
                    else:
                        screen.blit(tl[(i*j)%2], (y, x))
                    if (0, 1) in wallType:
                        screen.blit(wl, (y, x))
                    elif (0, -1) in wallType:
                        screen.blit(wr, (y, x))
                    elif (1, 0) in wallType:
                        screen.blit(wt, (y, x))
                    elif (-1, 0) in wallType:
                        screen.blit(wb, (y, x))
                elif len(wallType) == 2:
                    if(i+j)%2 == 0:
                        screen.blit(td[(i*j)%2], (y, x))
                    else:
                        screen.blit(tl[(i*j)%2], (y, x))
                    if (0, 1) in wallType:
                        if (1, 0) in wallType:
                            screen.blit(wlt, (y, x))
                        elif (-1, 0) in wallType:
                            screen.blit(wlb, (y, x))
                        else:
                            screen.blit(wtb, (y, x))
                    elif (0, -1) in wallType:
                        if (1, 0) in wallType:
                            screen.blit(wrt, (y, x))
                        elif (-1, 0) in wallType:
                            screen.blit(wrb, (y, x))
                    else:
                        screen.blit(wlr, (y, x))
                elif len(wallType) == 3:
                    if(i+j)%2 == 0:
                        screen.blit(td[(i*j)%2], (y, x))
                    else:
                        screen.blit(tl[(i*j)%2], (y, x))
                    if (0, 1) not in wallType:
                        screen.blit(w3r, (y, x))
                    elif (0, -1) not in wallType:
                        screen.blit(w3l, (y, x))
                    elif (1, 0) not in wallType:
                        screen.blit(w3b, (y, x))
                    elif (-1, 0) not in wallType:
                        screen.blit(w3t, (y, x))
                elif len(wallType) == 4:
                    if(i+j)%2 == 0:
                        screen.blit(td[(i*j)%2], (y, x))
                    else:
                        screen.blit(tl[(i*j)%2], (y, x))
                    screen.blit(w4, (y, x))

            elif(currLevel.matrix[i][j]) == 5:
                if(i+j)%2 == 0:
                    if currLevel.matrix[i-1][j] == 1:
                        screen.blit(tds[(i*j)%2], (y, x))
                    else:
                        screen.blit(td[(i*j)%2], (y, x))
                else:
                    if currLevel.matrix[i-1][j] == 1:
                        screen.blit(tls[(i*j)%2], (y, x))
                    else:
                        screen.blit(tl[(i*j)%2], (y, x))
                screen.blit(treasure, (y, x))
            elif(currLevel.matrix[i][j]) == 2:
                if(i+j)%2 == 0:
                    if currLevel.matrix[i-1][j] == 1:
                        screen.blit(tds[(i*j)%2], (y, x))
                    else:
                        screen.blit(td[(i*j)%2], (y, x))
                else:
                    if currLevel.matrix[i-1][j] == 1:
                        screen.blit(tls[(i*j)%2], (y, x))
                    else:
                        screen.blit(tl[(i*j)%2], (y, x))
                if(currLevel.playerY == i-1 and currLevel.playerX == j):
                    screen.blit(charS, (y, x))
                screen.blit(coin[animPtr%8], (y, x))
            elif(currLevel.matrix[i][j]) == 3:
                if(i+j)%2 == 0:
                    if currLevel.matrix[i-1][j] == 1:
                        screen.blit(tds[(i*j)%2], (y, x))
                    else:
                        screen.blit(td[(i*j)%2], (y, x))
                else:
                    if currLevel.matrix[i-1][j] == 1:
                        screen.blit(tls[(i*j)%2], (y, x))
                    else:
                        screen.blit(tl[(i*j)%2], (y, x))
                screen.blit(crate, (y, x))
            elif(currLevel.matrix[i][j]) == 0:
                if(i+j)%2 == 0:
                    if currLevel.matrix[i-1][j] == 1:
                        screen.blit(tds[(i*j)%2], (y, x))
                    else:
                        screen.blit(td[(i*j)%2], (y, x))
                else:
                    if currLevel.matrix[i-1][j] == 1:
                        screen.blit(tls[(i*j)%2-1], (y, x))
                    else:
                        screen.blit(tl[(i*j)%2], (y, x))
                if(currLevel.playerY == i-1 and currLevel.playerX == j):
                    screen.blit(charS, (y, x))
            if(currLevel.playerX == j and currLevel.playerY == i):
                screen.blit(char[animPtr%2], (y, x))
            y += 32
        x += 32
    screen.blit(bfsBtn, (45.5, 360))
    screen.blit(aStarBtn, (169, 360))
    screen.blit(dfsBtn, (292.5, 360))

def automator(moves, state, screen):
    global animPtr
    for step in moves:
        pygame.time.wait(100)
        move(state, step)
        screen.fill((53, 73, 94))
        animPtr += 1
        render(state, screen)
        pygame.display.update()

def gameScreen(currLevel, levelIndex):
    buffer = 0
    global animPtr
    pygame.init()
    pygame.display.set_caption("SokoBot")
    pygame.display.set_icon(icon)
    screen2 = pygame.display.set_mode((416, 416))
    end = False
    while not end:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if isLegal(currLevel, (0, -1)):
                        vals = (0, -1)
                        move(currLevel, vals)
                elif event.key == pygame.K_DOWN:
                    if isLegal(currLevel, (0, 1)):
                        vals = (0, 1)
                        move(currLevel, vals)
                elif event.key == pygame.K_LEFT:
                    if isLegal(currLevel, (-1, 0)):
                        vals = (-1, 0)
                        move(currLevel, vals)
                elif event.key == pygame.K_RIGHT:
                    if isLegal(currLevel, (1, 0)):
                        vals = (1, 0)
                        move(currLevel, vals)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 45.5 <= mouse[0] <= 123.5 and 360 <= mouse[1] <= 393:
                    currLevel = copy.deepcopy(levels[levelIndex])
                    solution = breadthFirstSearch(currLevel).timeLine
                    if solution:
                        t1 = Thread(target = automator, args = (solution, currLevel, screen2))
                        t1.start()
                        t1.join()
                if 169 <= mouse[0] <= 247 and 360 <= mouse[1] <= 393:
                    currLevel = copy.deepcopy(levels[levelIndex])
                    solution = aStarManhattan(currLevel).timeLine
                    if solution:
                        t1 = Thread(target = automator, args = (solution, currLevel, screen2))
                        t1.start()
                        t1.join()
                if 292.5 <= mouse[0] <= 370.5 and 360 <= mouse[1] <= 393:
                    currLevel = copy.deepcopy(levels[levelIndex])
                    solution = depthFirstSearch(currLevel).timeLine
                    if solution:
                        t1 = Thread(target = automator, args = (solution, currLevel, screen2))
                        t1.start()
                        t1.join()
            if check(currLevel):
                levelIndex += 1
                print("Level Cleared!")
                if levelIndex == 6:
                    levelIndex = 0
                currLevel = copy.deepcopy(levels[levelIndex])
        screen2.fill((53, 73, 94))
        buffer += 1
        if not buffer%4:
            animPtr += 1
        render(currLevel, screen2)
        pygame.display.update()

def startScreen():
    end = False
    pygame.init()
    color = (255, 0, 0)
    screen1 = pygame.display.set_mode((416, 416))
    screen1.fill((255, 255, 255))
    while not end:
        clock.tick(6)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        pygame.display.update()

# startScreen()
gameScreen(currLevel, levelIndex)