import time
import copy
from funcs import *

stack = []
possibleMoves = ((0, 1), (1, 0), (0, -1), (-1, 0))
stateHist = []
solution = []

timeLimit = 25

def depthFirstSearch(boardState):
    stack.append(copy.deepcopy(boardState))
    timeStart = time.time()
    while time.time() < timeStart + timeLimit:
        lastState = stack.pop()
        if check(lastState):
            print("Solved in", time.time()-timeStart, "secs", sep = " ")
            # moveDictation(lastState.timeLine)
            return lastState
        for step in possibleMoves:
            newState = copy.deepcopy(lastState)
            if isLegal(newState, step) and not blocked(newState, step):
                move(newState, step)
                if not searchHist(newState, stateHist):
                    stack.append(newState)
                    stateHist.append(newState)
    print("Time limit of", timeLimit, "secs exceeded")
    return 0
            