from queue import PriorityQueue
import time
import copy
from funcs import *

pq = PriorityQueue()
possibleMoves = ((0, 1), (1, 0), (0, -1), (-1, 0))
stateHist = []

timeLimit = 32

def aStarManhattan(gameState):
    hx = 0
    for i in range(0, gameState.rows):
        for j in range(0, gameState.cols):
            if gameState.matrix[i][j] == 3:
                hx += min(manhattanDist(gameState, (i, j)))
    pq.put((hx, id(gameState), gameState))
    timeStart = time.time()
    while time.time() < timeStart + timeLimit:
        lastState = pq.get()[2]
        if check(lastState):
            print("Solved in", time.time()-timeStart, "secs", sep = " ")
            return lastState
        for step in possibleMoves:
            newState = copy.deepcopy(lastState)
            if isLegal(newState, step) and not blocked(newState, step):
                move(newState, step)
                if not searchHist(newState, stateHist):
                    hx = 0
                    for i in range(0, gameState.rows):
                        for j in range(0, gameState.cols):
                            if gameState.matrix[i][j] == 3:
                                hx += min(manhattanDist(gameState, (i, j)))
                    pq.put((hx, id(newState),newState))
                    stateHist.append(newState)
    print("Time limit of", timeLimit, "secs exceeded")
    return 0
