def multMat(mNew, mOrig):
	newMat = [[1e9]*len(matrixOrig) for i in range(len(matrixOrig[0]))]
	length = len(mNew[0])
	for x in range(length):
		for y in range(length):
			vals = []
			for i in range(length):
				vals.append(mNew[i][y] + mOrig[x][i])
			#if count == 1: print min(vals), x, y
			newMat[x][y] = min(vals)
			#if count == 1: print newMat
			
	#if count ==1:
		#print mNew
		#print mOrig
		#print newMat
	ASSP(newMat)

			
def ASSP(matrix):
	global count
	length = len(matrix[0])
	for x in range(length):
		for y in range(length):
			if matrix[x][y] < optMat[x][y]:
				optMat[x][y] = matrix[x][y]
	if count <= len(matrix):
		count+=1
		multMat(matrix, matrixOrig)
	else:
		return True



matrixOrig = [[0, 55, -1, 87, 52, 22, 17, 15, 15, -1, 18, -1],
[55, 0, 56, -1, 96, 6, -1, 15, 5, 14, 12, -1],
[-1, 56, 0, 88, 15, 13, 48, 67, -1, 41, -1, 9],
[87, -1, 88, 0, -1, -1, -1, -1, -1, 15, -1, 14],
[52, 96, 15, -1, 0, 10, 61, -1, 15, -1, 79, 85],
[22, 6, 13, -1, 10, 0, -1, 70, 13, 5, -1, -1],
[17, -1, 48, -1, 61, -1, 0, -1, -1, 12, 6, 20],
[15, 15, 67, -1, -1, 70, -1, 0, 14, -1, 14, 12],
[15, 5, -1, -1, 15, 13, -1, 14, 0, -1, 85, -1],
[-1, 14, 41, 15, -1, 5, 12, -1, -1, 0, 84, 64],
[18, 12, -1, -1, 79, -1, 6, 14, 85, 84, 0, 56],
[-1, -1, 9, 14, 85, -1, 20, 12, -1, 64, 56, 0]]

count = 0
optMat = [[1e9]*len(matrixOrig) for i in range(len(matrixOrig[0]))]
length = len(matrixOrig[0])
for x in range(length):
	for y in range(length):
		if matrixOrig[x][y] == -1:
			matrixOrig[x][y] = 1e9
		if matrixOrig[x][y] == 0:
			matrixOrig[x][y] = 1e8

ASSP(matrixOrig)
for x in range(length):
	for y in range(length):
		if x == y:
			optMat[x][y] = 0

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in optMat]))
