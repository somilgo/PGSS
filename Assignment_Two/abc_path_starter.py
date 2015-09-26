from pprint import pprint
import copy

class State(): pass

def print_board(board):
  """Just give us a board, and we'll print it as a 2D array"""
  pprint(board, width = 55)

def make_state(board, x, y, letter, next_letter):
  """Allows you to make a state given a board, the x and y position of the most
     recently added letter, the value of the most recently added letter, and the
     value of the next letter"""
  state = State()
  state.board = board
  state.head_x = x
  state.head_y = y
  state.head_letter = letter
  state.next_letter = next_letter
  return state

def get_starting_board(constraints, a_location):
  """Takes the constraint string and location of "A" and returns a 7x7 array
     with letters in their proper positions along the border and "A" set in its
     correct position.

    NOTE:  BLANK POSITIONS ARE SET AS A STRING OF '0'. YOU CAN USE THIS TO DETECT A
    BLANK SPACE VS. AN OCCUPIED SPACE."""
  board = [['0']*7 for x in range(7)]
  index = 0
  for x in range(7):
    board[0][x] = constraints[index]
    index += 1

  for row in range(1, 7):
    board[row][x] = constraints[index]
    index += 1

  for col in reversed(range(6)):
    board[6][col] = constraints[index]
    index += 1

  for row in reversed(range(1, 6)):
    board[row][0] = constraints[index]
    index += 1

  board[a_location[0]][a_location[1]] = "A"
  return board


def is_legal_position(x, y, letter, board):
  """Given a board, a letter, and a position, determine if that letter is allowed to go in that position.
     There are several things to keep in mind:
        a) It may be living in a suitable column
        b) It may be living in a suitable row
        c) It may be living in a suitable diagonal
        d) It may be trying to overwrite a non-blank position

     This should probably just return either True or False
     """

  if board[x][y] != '0':
    return False

  if board[0][y] == letter or board[6][y] == letter:
    return True
  elif board[x][0] == letter or board[x][6] == letter:
    return True
  elif x==y and (board[0][0] == letter or board[6][6] == letter):
    return True
  elif x+y==6 and (board[0][6] == letter or board[6][0] == letter):
    return True

  return False

# a list of valid places to look when you're trying to add the next letter.  Basically, each index
# corresponds to
# 0 1 2
# 3 X 4
# 5 6 7
# So if you're trying to make the move at index 0 (which is the move (-1, -1))
# and you're currently standing at board[3][3],
# then your next move would be at board[2][2].
moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def get_children(state):
  """ Takes a state and returns a list of children states for the parent state.  This should probably somehow
      call the "is_legal_move" method seen above.

      NOTE:  Please be careful about copying the board.  Python's copy library has been imported for you,
      so when you want to make a copy of a board, you can just call copy.deepcopy(board) [for example]
  """
  children = []
  newLetter = state.next_letter
  newNext = alpha[(alpha.index(state.next_letter)+1)]

  for m in moves:
    x = state.head_x + m[0]
    y = state.head_y + m[1]
    if is_legal_position(x, y, state.next_letter, state.board):
      chBoard = copy.deepcopy(state.board)
      chBoard[x][y] = state.next_letter
      children.append(make_state(chBoard, x, y, newLetter, newNext))

  return children

def solve_with_helper(state):
  children = get_children(state)
  for c in children:
    if not any('0' in b for b in c.board):
      return c
    trial = solve_with_helper(c)
    if trial != None:
      return trial
def solveABC(constraints, a_location):
  # get the starting board from our provided function
  board = get_starting_board(constraints, a_location)

  # make a starting state with our provided function
  start_state = make_state(board, a_location[0], a_location[1], "A", "B")

  # return the result from your solver
  result = solve_with_helper(start_state)

  # return that resulting board
  return result.board

# give it the constraints and an (x, y) pair of where A starts in the 7x7 board

# note that this puzzle does have a valid solution, so if your program is working,
# it should be able to find it =)
explored = 0
print_board(solveABC("NROJDCWVTKGELYXMIPFHBSQU", (3, 5)))