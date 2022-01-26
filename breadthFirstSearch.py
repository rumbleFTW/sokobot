import collections
import time
import copy
from funcs import *

q = collections.deque([])
possibleMoves = ((0, 1), (1, 0), (0, -1), (-1, 0))
stateHist = []

timeLimit = 180

def breadthFirstSearch(boardState):
    q.append(copy.deepcopy(boardState))
    timeStart = time.time()
    while time.time() < timeStart + timeLimit:
        lastState = q.popleft()
        if check(lastState):
            print("Solved in", time.time()-timeStart, "secs", sep = " ")
            # moveDictation(lastState.timeLine)
            return lastState
        for step in possibleMoves:
            newState = copy.deepcopy(lastState)
            if isLegal(newState, step) and not blocked(newState, step):
                move(newState, step)
                if not searchHist(newState, stateHist):
                    q.append(newState)
                    stateHist.append(newState)
    print("Time limit of", timeLimit, "secs exceeded")
    return 0