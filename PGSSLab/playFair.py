import copy

#Open file and save to a string
file = open('tester.txt', 'r')
code = file.read()

#The key (currently unknown)
key = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
keyTable = []

#Convert key into a 2D array
row = []
letterCount = 0
for i in key:
    letterCount += 1
    row.append(i)
    if letterCount == 5:
        keyTable.append(tuple(row))
        letterCount = 0
        row = []

dec = ""
pair = []
pairCoords = []
for s in code:
    if s == "J":
        s = "I"
    if s == " ":
        continue
    pair.append(s)
    tempCoords = []
    for i in range(5):
        if s in keyTable[i]:
            pairCoords.append(i)
            pairCoords.append(keyTable[i].index(s))
    if len(pair) == 2:
        noCoor = True
        #Checks for it being at end of column
        coords = copy.deepcopy(pairCoords)
        if pairCoords[0] == 0 and pairCoords[1] != 0:
            coords[0] = 4
            #coords[1] -= 1
        if pairCoords[2] == 0 and pairCoords[3] != 0:
            coords[2] = 4
            #coords[3] -= 1
        #Checks for same column case
        if coords[1] == coords[3]:
            dec += keyTable[coords[0]-1][coords[1]]
            dec += keyTable[coords[2]-1][coords[3]]
            noCoor = False

        #Checks for it being at end of row
        coords = copy.deepcopy(pairCoords)
        if pairCoords[1] == 0 and pairCoords[0] != 0:
            coords[1] = 4
            #coords[0] -= 1
        if pairCoords[3] == 0 and pairCoords[2] != 0:
            coords[3] = 4
            #coords[2] -= 1
        if coords[0] == coords[2]:
            dec += keyTable[coords[0]][coords[1]-1]
            dec += keyTable[coords[2]][coords[3]-1]
            noCoor = False

        #If there is no common row or column
        if noCoor:
            # print keyTable[pairCoords[0]][pairCoords[3]]
            # print keyTable[pairCoords[2]][pairCoords[1]]
            dec+= keyTable[pairCoords[0]][pairCoords[3]]
            dec+= keyTable[pairCoords[2]][pairCoords[1]]
        pairCoords = []
        pair = []

print dec


