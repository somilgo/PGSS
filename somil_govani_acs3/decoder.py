import string
import random
import enchant
import ngram as ns
import copy

def randomKeyGen():
	key = {}
	alphas = list(string.ascii_uppercase)
	for i in string.ascii_uppercase:
		randLetter = alphas[random.randint(0,len(alphas)-1)]
		while (randLetter == i):
			randLetter = alphas[random.randint(0,len(alphas)-1)]
		key[i] = randLetter
		alphas.remove(randLetter)
	return key

def heuristic(line):
	score = 0
	n = 5
	code = [line[i:i+n] for i in range(0, len(line), n)]
	code = code.remove(code[random.randint(-1, 6)])
	for i in [line[i:i+n] for i in range(0, len(line), n)]:
		if d.check(i):
			#print i
			score += 1
	return score

def keyChange(key):
	index1 = random.randint(0,25)
	index2 = random.randint(0,25)
	while index1 == index2:
		index2 = random.randint(0,25)
	newKey = copy.deepcopy(key)
	newKey[alphas[index1]] = key[alphas[index2]]
	newKey[alphas[index2]] = key[alphas[index1]]
	return newKey

def decrypt(code, key):
	result = ""
	for i in code:
		result+=key[i]
	return result

def run(key, parentScore):
	parent = key
	score = parentScore
	new = keyChange(parent)
	newScore = fitness.score(decrypt(code, new))
	while newScore <= score:
		new = keyChange(parent)
		newScore = fitness.score(decrypt(code, new))
	print new
	print newScore
	run(new, newScore)

def encrypt(text):
	key = randomKeyGen()
	result = ""
	for i in text:
		result+=key[i]
	return result
	

#Write text to string
file = open('enc.txt', 'r')
code = file.read().upper()

alphas = list(string.ascii_uppercase)
d = enchant.Dict("en_US")

decodedText = decrypt(code, {'A': 'D', 'C': 'R', 'B': 'Q', 'E': 'N', 'D': 'P', 'G': 'Z', 'F': 'T', 'I': 'M', 'H': 'U', 'K': 'I', 'J': 'O', 'M': 'E', 'L': 'C', 'O': 'G', 'N': 'K', 'Q': 'B', 'P': 'A', 'S': 'J', 'R': 'V', 'U': 'W', 'T': 'X', 'W': 'H', 'V': 'S', 'Y': 'Y', 'X': 'L', 'Z': 'F'})
text_file = open("decodedText.txt", "w")
text_file.write(decodedText)
text_file.close()
fitness = ns.ngram_score('english_quadgrams.txt')
first = randomKeyGen()
#used to find key
#run(first, fitness.score(decrypt(code, first)))