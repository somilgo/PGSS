#Somil Govani
#Collaborated with Milind J., Sameer L, Parris A.

import copy
from heapq import *
exploredStates = 0

#make an empty board:
def make2dList(rows, cols):
  a = []
  for row in range(rows): a += [[0]*cols]
  return a

# print make2dList(4, 5)

#make the goal board (square)
def makeGoalBoard(n):
  board = make2dList(n, n)
  counter = 1
  for row in range(n):
    for col in range(n):
      board[row][col] = counter
      counter += 1
  board[n-1][n-1] = 0
  return board

def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in xrange(rows):
        for col in xrange(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen

def print2dList(a):
    if (a == []):
        # So we don't crash accessing a[0]
        print []
        return
    rows = len(a)
    cols = len(a[0])
    fieldWidth = maxItemLength(a)
    print "[ ",
    for row in xrange(rows):
        if (row > 0): print "\n  ",
        print "[ ",
        for col in xrange(cols):
            if (col > 0): print ",",
            # The next 2 lines print a[row][col] with the given fieldWidth
            format = "%" + str(fieldWidth) + "s"
            print format % str(a[row][col]),
        print "]",
    print "]"

def printBoard(board):
    print2dList(board)

#print2dList(makeGoalBoard(3))

class Struct(): pass

def makeState(board, parent=None, move=None, blankPosition=None):
  state = Struct()
  state.board = board
  state.parent = parent
  state.move = move
  state.moveCount = 0
  state.score = 100
  if (blankPosition == None):
    blankPosition = findBlankPosition(board)
  state.blankPosition = blankPosition
  return state

def findBlankPosition(board):
  n = len(board)
  for x in range(n):
    for y in range(n):
      if board[x][y] == 0:
        return x, y
  return None

#print findBlankPosition(makeGoalBoard(3))

#goalBoardState = makeState(makeGoalBoard(3))
#print2dList(goalBoardState.board)
#print goalBoardState.blankPosition

def printState(state):
  print "STATE: "
  print "move = ", state.move
  print "board = "
  print2dList(state.board)

#printState(makeState(makeGoalBoard(3)))


def isGoalState(state):
  n = len(state.board)
  counter = 1
  for row in range(n):
    for col in range(n):
      if (state.board[row][col] != counter%(n**2)):
        return False
      counter += 1
  return True

#print isGoalState(makeState(makeGoalBoard(3)))

moveDirs = [(-1,0),(1,0),(0,-1),(0,1)]
moveNames = ["up","down","left","right"]

def getMoveDir(moveName):
  return moveDirs[moveNames.index(moveName)]

#print getMoveDir("up")

def getChildren(state):
  n = len(state.board)
  children = []
  (blankRow, blankCol) = state.blankPosition
  for moveName in moveNames:
    (drow, dcol) = getMoveDir(moveName)
    (newBlankRow, newBlankCol) = (blankRow + drow, blankCol + dcol)
    if ((newBlankRow >= 0) and (newBlankRow < n) and (newBlankCol >= 0) and (newBlankCol < n)):
      newBoard = copy.deepcopy(state.board)
      newBoard = [list(row) for row in newBoard]
      temp = newBoard[newBlankRow][newBlankCol]
      newBoard[blankRow][blankCol] = temp
      newBoard[newBlankRow][newBlankCol] = 0
      newBoard = tuple([tuple(row) for row in newBoard])
      newState = makeState(newBoard, state, moveName, (newBlankRow, newBlankCol))
      children.append(newState)
  return children

#for child in getChildren(makeState(makeGoalBoard(3))):
#  print2dList(child.board)

def findGoalWithDepthFirstSearch(state):
  global exploredStates
  exploredStates = 0
  result = findGoalWithDepthFirstSearchHelper(state)
  print "Explored states: ", exploredStates
  return result

def findGoalWithDepthFirstSearchHelper(state):
  global exploredStates
  seenBoards = set()
  if (isGoalState(state)):
    print "goal state! yay!"
    return state
  queue = [ state ]
  while len(queue) > 0:
    state = queue.pop(-1)
    for child in getChildren(state):
      if (isGoalState(child)):
        return child
      elif (child.board not in seenBoards):
        seenBoards.add(child.board)
        queue.append(child)
        exploredStates += 1
        if exploredStates%1000 == 0:
          print "Still searching on board number ", exploredStates
  return None

def getMovesToState(state):
  moves = []
  while (state.move != None):
    moves.append(state.move)
    state = state.parent
  return list(reversed(moves))

# board = makeState([[1,2,3],[4,5,6],[0,7,8]])
# solution = findGoalWithDepthFirstSearch(board)
# print getMovesToState(solution)

## HEY!  RUNNING THIS MIGHT CRASH YOUR PYTHON INTERPRETER
## ... SO WE RECOMMEND YOU DON'T RUN IT =)
# board = makeState([[1,2,3],[5,7,6],[4,0,8]])
# solution = findGoalWithDepthFirstSearch(board)
# print getMovesToState(solution)

# Including these functions just so you'll have some available
# examples of how to push into a queue (and pop from) with and
# without a heuristic value
def push_without_heuristic():
  class EightBoard(): pass
  b1 = EightBoard()
  b1.board = [["b1", 1]]

  b2 = EightBoard()
  b2.board = [["b2",3],[0,2]]

  b3 = EightBoard()
  b3.board = [["b3", 2],[1,3]]

  queue = []

  heappush(queue, b1)
  heappush(queue, b2)
  heappush(queue, b3)

  something1 = heappop(queue)

  print something1.board

#push_without_heuristic()

def push_with_heuristic():
  class EightBoard(): pass
  b1 = EightBoard()
  b1.board = [["b1",2],[3,0]]

  b2 = EightBoard()
  b2.board = [["b2",3],[0,2]]

  b3 = EightBoard()
  b3.board = [["b3", 2],[1,3]]

  queue = []

  heappush(queue, (10, b1))
  heappush(queue, (20, b2))
  heappush(queue, (15, b3))

  something1 = heappop(queue)
  something2 = heappop(queue)
  print something1[1].board
  print something2[1].board

#push_with_heuristic()

# Your A* function can go here :)

def score(state, goal):
  sum = 0
  row = len(state)
  column = len(state[0])
  for r in range(row):
    for c in range(column):
      num = state[r][c]
      for i in range(row):
        if num in goal[i]:
          sum += abs(r-i) + abs(c-goal[i].index(num))
  return sum

def solveWithAStar(state):
  global exploredStates
  exploredStates = 0
  result = AHelper(state)
  print "Explored states: ", exploredStates
  return result

def AHelper(state):
  global exploredStates
  seenBoards = set()
  if (isGoalState(state)):
    print "goal state! yay!"
    return state
  queue = [ state ]
  goal = [[1,2,3],[4,5,6],[7,8,0]]
  while len(queue) > 0:
    topScore = 1e9
    for i in queue:
      if i.score < topScore:
        state = i
        topScore = i.score
    queue.remove(state)
    for child in getChildren(state):
      child.moveCount = child.parent.moveCount + 1
      if (isGoalState(child)):
        return child
      elif (child.board not in seenBoards):
        child.score = score(child.board, goal) + child.moveCount
        seenBoards.add(child.board)
        queue.append(child)
        exploredStates += 1
        if exploredStates%1000 == 0:
          print "Still searching on board number ", exploredStates
  return None

board = makeState([[1, 2, 3],[4, 7, 0],[5, 6, 8]])
# test = [[1,2,3],[4, 5, 6],[0,7,8]]
# goal = [[1,2,3],[4,5,6],[7,8,0]]


solution = solveWithAStar(board)
print getMovesToState(solution)