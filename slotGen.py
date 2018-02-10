# Only says part of the word
# Find time that alexa listens before going to response
# Generate Stuttered words

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



print generateStutter("cat")