pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
new_wordc = word[1:] + word[0] + str(pyg)
new_wordv = str(word) + str(pyg)
if len(original) > 0 and original.isalpha():
	print word
	if first == "a" or first == "e" or first == "i" or first == "o" or first == "u": 
		print new_wordv
	else:
		print new_wordc
