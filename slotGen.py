def splitAtVowel(word):
	wordPossibilities = []
	# This simulates stuttering
	vowels = list("aeiou")
	for i, letter in enumerate(word):
		if letter in vowels:
			print(word[:i] + ' ' + word)
			#print(word[:i])

splitAtVowel("calculator")
