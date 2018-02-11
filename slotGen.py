# Only says part of the word
# Find time that alexa listens before going to response
# Generate Stuttered words
import itertools
import string
import json
def indexOfNextVowel(partialWord, i):
	for letter in partialWord:
		if letter in list("aeiou"):
			return partialWord.index(letter) + i

def indexOfPreviousVowel(partialWord, i):
	return

def splitAtVowel(word):
	# This splits words at every point in which the person may stutter
	wordPossibilities = []
	for i, letter in enumerate(list(word)):
		if letter not in list("aeiou"):
			if i+1 < len(word):
				newWord = letter
				i += 1
				nextLetter = list(word)[i]
				while nextLetter not in list("aeiou"):
					newWord = newWord + nextLetter
					i += 1
					if i < len(word):
						nextLetter = word[i]
					else:
						break
				wordPossibilities.append(newWord)
	return list(set(wordPossibilities))

def generateStutter(word):
	wordList = []
	for i, letter in enumerate(word):
		for e in range(2):
			wordList.append(str(word[:i] + " " + letter + " " + word[i:]).strip())
			letter = letter + " " + letter
	for val in splitAtVowel(word):
		wordList.append(str(word[:word.index(val)] + " " + val + " " + word[word.index(val):]).strip())
	return list(set(wordList))

def generatePartialWords(word):
	wordList = []
	for i in range(1,len(word) + 1):
		wordList.append(word[:i])
	return wordList

def convertWtoP(word):
	return word.replace("w", )

def genAllSpeechPatterns(sentence):
	info = {}
	for wordValue in sentence.split(" "):
		if len(wordValue) > 0:
			info[wordValue] = {}
			for word in generateStutter(wordValue):
				if word not in info[wordValue].itervalues():
					info[wordValue][word] = []
					info[wordValue][wordValue] = []
				if word != wordValue:
					info[wordValue][word].append("Stutter")
			for word in generatePartialWords(wordValue):
				if word not in info[wordValue].itervalues():
					info[wordValue][word] = []
				if word != wordValue:
					info[wordValue][word].append("Partial")
	return info

#def gene

#def genSpeechPattern(input, output):


#print generateStutter("cat")
#a = genAllSpeechPatterns("this game is incomprehensible")
allWords = ' '.join(open("listOfSentences.txt").read().split("\n")).translate(None, string.punctuation).lower()
print genAllSpeechPatterns(allWords)
with open('result.json', 'w') as fp:
	json.dump(genAllSpeechPatterns(allWords), fp)
