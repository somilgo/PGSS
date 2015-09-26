def minimalSpanningTree(matrix):
	global weight
	length = len(matrix[0])
	minVal = 1e8
	xval = None
	yval = None
	if weight == 0:
		for x in range(length):
			for y in range(length):
				node = matrix[x][y]
				if (node < minVal):
					minVal = node
					xval = x
					yval = y
	else:
		for x in range(length):
			for y in range(length):
				node = matrix[x][y]
				if (node < minVal) and (x not in used) and (y in used):
					minVal = node
					xval = x
					yval = y
	if xval == None or yval == None:
		return True
	weight+=minVal
	used.append(xval)
	used.append(yval)
	#print(xval, yval)
	matrix[xval][yval] = 1e9
	matrix[yval][xval] = 1e9
	minimalSpanningTree(matrix)

weight = 0
used = []
matrix = [[ 0, 23, 16, 28, 23, 19, 40, 18],
[23, 0, 29, 32, 48, 50, 43, 34],
[16, 29, 0, 25, 41, 27, 23, 12],
[28, 32, 25, 0, 28, 27, 40, 37],
[23, 48, 41, 28, 0, 42, 40, 15],
[19, 50, 27, 27, 42, 0, 27, 49],
[40, 43, 23, 40, 40, 27, 0, 20],
[18, 34, 12, 37, 15, 49, 20, 0]]
length = len(matrix[0])
for x in range(length):
	for y in range(length):
		if matrix[x][y] == 0:
			matrix[x][y] = 1e9
#print matrix
minimalSpanningTree(matrix)
print "The weight of the minimal spanning tree is: " + str(weight)