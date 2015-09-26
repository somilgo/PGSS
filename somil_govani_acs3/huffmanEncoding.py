import operator

def fixedLengthSize(message):
	listOfChar = charList(message)
	return (len("{0:#b}".format(len(listOfChar))) - 2) * len(message)

def charList(message):
	chars = {}
	for m in message:
		if m not in chars:
			chars[m] = 0
		chars[m]+=1
	return chars

def mapping(chars):
	maxChar = max(chars.iteritems(), key=operator.itemgetter(1))[0]
	for i in charBins:
		if i in chars:
			if maxChar == i:
				charBins[i] = charBins[i] + "0"
			else:
				charBins[i] = charBins[i] + "1"
	del chars[maxChar]
	if len(chars) == 1:
		return charBins
	else:
		return mapping(chars)



message = "HEX99CC99HEX99BD99HEX99BD99HEX99FA99"
#message = "sushigo"
print "The length of the message assuming fixed length identifiers is: " + str(fixedLengthSize(message))
charBins = {}
chars = charList(message)
for c in chars:
	charBins[c] = ""
print mapping(chars)
print "\nThe original message: " + message
newMess = ""
for i in message:
	newMess += charBins[i]
print "Huffman Encoded Message: " + newMess

