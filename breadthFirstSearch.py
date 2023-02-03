import time
import copy
from funcs import *

q = []
possibleMoves = ((0, 1), (1, 0), (0, -1), (-1, 0))
stateHist = []

timeLimit = 180

def breadthFirstSearch(boardState):
    q.append(copy.deepcopy(boardState))
    timeStart = time.time()
    while time.time() < timeStart + timeLimit:
        lastState = q.pop(0)
        if check(lastState):                                 # If state is solved
            print("Solved in", time.time()-timeStart, "secs", sep = " ")
            # moveDictation(lastState.timeLine)
            return lastState
        for step in possibleMoves:                          # Trying out each possible move
            newState = copy.deepcopy(lastState)
            if isLegal(newState, step) and not blocked(newState, step): # Pruning out of bounds and unsolvable states
                move(newState, step)
                if not searchHist(newState, stateHist):     # Adding to queue if state not in queue
                    q.append(newState)
                    stateHist.append(newState)
    print("Time limit of", timeLimit, "secs exceeded")
    return boardState