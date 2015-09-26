def printBoard(board):
	for i in board:
		print i

#Convert the message to a 2D list
def errorDetect (message):
	block = []
	tempBlock = []
	width = int(len(message) ** .5)
	count = 0
	for i in message:
		tempBlock.append(int(i))
		count += 1
		if count >= width:
			block.append(tempBlock)
			tempBlock = []
			count = 0

	errRow = None
	errCol = None
	summ = 0
	swap = [1,0]

	for l in block[:-1]:
		for n in range(width-1):
			summ += l[n]

		if not int("{0:b}".format(summ)[-1:]) == l[width-1]:
			errRow = block.index(l)
		summ = 0

	for f in range(width-1):
		for s in block[:-1]:
			summ+=s[f]
		if not int("{0:b}".format(summ)[-1:]) == block[width-1][f]:
			errCol = f
		summ = 0

	if errRow != None and errCol != None:
		print "Fixed message..."
		block[errRow][errCol] = swap[block[errRow][errCol]]
		printBoard(block)
	else:
		print "No Error!"

errorDetect(raw_input("Error Message: "))
