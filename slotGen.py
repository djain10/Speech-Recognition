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
					print i
					if i < len(word):
						nextLetter = word[i]
					else:
						break
				wordPossibilities.append(newWord)
	return wordPossibilities

print splitAtVowel("catastrophic")
