def swap(alphabet, string):
	swapped_string = ''

	for letter in string:
		if not letter in alphabet:
			# print('Error!')
			continue

		swapped_string += alphabet[letter]
	
	return swapped_string
