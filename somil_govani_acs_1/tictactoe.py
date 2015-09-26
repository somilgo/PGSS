#PGSS TIC-TAC-TOE

import copy

class Struct(): pass

class Board:
    """basic tic-tac-toe game
    """

    def __init__(self, parent = None):
        """ Construct TTT
        """
        self.data = [[' ']*3 for row in range(3)]
        self.parent = parent

    def __str__(self):
        """text representation of the board
        """
        b = '-------\n'
        for i in range(3):
            b+='|'
            for j in range(3):
                b+= self.data[i][j] + '|'
            b+='\n-------\n'
        return b

    def getBoard(self):
        """get the 2D array of data
        """
        return self.data

    def move(self, row, col, mark):
        """If the chosen position is open and the row and col
            are within range, places the mark in the 2Darray at [row][col]
        """
        if (row in range(3) and col in range(3)):
            if (self.data[row][col] == " "):
                if (mark == "X"):
                    self.data[row][col] = "X"
                elif (mark == "O"):
                    self.data[row][col] = "O"
                return True
            else:
                print("This spot is taken, choose again")
                return False
        print("col or row not in range, choose again")
        return False

    def isTie(self, board):
        """returns true if the board is full and false if otherwise
        """
        for i in range(3):
            for j in  range(3):
                if (board[i][j] == " "):
                    return False
        return True

    def isWinFor(self, board, mark):
        """returns true if "mark" has won the game and false otherwise
        """
        rowWin = 0
        colWin = 0
        for i in range(3):
            rowWin = 0
            colWin = 0
            for j in range(3):
                if (board[i][j] == mark):
                    rowWin +=1
                if (board[j][i] == mark):
                    colWin +=1
            if (colWin == 3 or rowWin == 3):
                return True
        if (board[0][0] == board[1][1] == board[2][2] == mark):
           return True
        if (board[0][2] == board[1][1] == board[2][0] == mark):
            return True
        return False

    def compareBoards(self, other):
        """A method to check if self has an equivalent board to "other",
            returns true if all marks are in equivalent positions, otherwise false.
        """
        for row in range(3):
            for col in range(3):
                if self.data[row][col] != other.getBoard()[row][col]:
                    return False
        return True

    def newMark(self, mark):
        """returns an X if input "mark" was O, returns O otherwise
        """
        if mark == "X":
            return "O"
        return "X"


    def playTTT(self):
        """plays interactive Tic-Tac-Toe in the shell with our board
        """
        currentMark = "X"
        print("Welcome to Tic-Tac-Toe!")
        while(True):
                print(self)
                while(True):
                  if currentMark == "X":
                    row = int(input("Enter a row (0, 1, or 2): "))
                    col = int(input("Enter a col (0, 1, or 2): "))
                  else:
                    # this method is going to break the first time you run the program
                    # it's supposed to be like that =)
                    # all you have to do is implement minimax logic in this function and
                    # return the row and column index of the best move.  good luck!
                    row, col = self.get_ai_move()
                  if(self.move(row,col, currentMark)):
                      break
                if (self.isWinFor(self.data, currentMark)):
                    print(self)
                    print currentMark + " wins!"
                    break
                elif self.isTie(self.data):
                  print(self)
                  print "It's a tie!"
                  break
                currentMark = self.newMark(currentMark)

    def make_ttt_state(self, data, parent, move, belongs_to_o, value):
      state = Struct()
      state.data = data
      state.parent = parent
      state.move = move
      state.belongs_to_o = belongs_to_o #time for o to make a move
      state.value = value
      return state

    def get_children_of(self, state):
      data = state.data
      children = []
      for x in range(3):
        for y in range(3):
          data_copy = copy.deepcopy(data)
          if data_copy[x][y] == " ":
            if state.belongs_to_o:
              data_copy[x][y] = "O"
            else:
              data_copy[x][y] = "X"
            if self.isWinFor(data_copy, "O"):
              val = 1
            elif self.isWinFor(data_copy, "X"):
              val = -1
            elif self.isTie(data_copy):
              val = 0
            else:
              val = None
            new_state = self.make_ttt_state(data_copy, state, (x, y), not state.belongs_to_o, val)
            children.append(new_state)
      return children


    def upVal(self, node):
    	if node.belongs_to_o: node.value = -2
    	if not node.belongs_to_o: node.value = 2
    	children = self.get_children_of(node)
    	for c in children:
    		if c.value == None:
    			self.upVal(c)
    		if node.belongs_to_o and c.value == 1:
    			node.value = 1
    			break
    		elif not node.belongs_to_o and c.value == -1:
    			node.value = -1
    			break
    		elif node.belongs_to_o:
    			node.value = max([node.value, c.value])
    		else:
    			node.value = min([node.value, c.value])
    	
   	

    def get_ai_move(self):
      # you need to fill in this method yourself!
      node = self.make_ttt_state(self.data, None, None, True, None)
      children = self.get_children_of(node)
      maxVal = -2
      move = 0, 0
      for c in children:
      	if c.value == 1:
      		return c.move
      	else:
      		self.upVal(c)
      for i in children:
      	if i.value > maxVal:
      		maxVal = i.value
      		move = i.move
      return move


b = Board()
b.playTTT()