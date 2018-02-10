def splitAtVowel(word):
	# This simulates stuttering
	vowels = list("aeiou")
	for letter in word:
		if letter in vowels:
			print("Vowels in this word")
splitAtVowel("car")
