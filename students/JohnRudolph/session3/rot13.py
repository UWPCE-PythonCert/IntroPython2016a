
def getnumref(let):
	'''
	This function accepts any ASCII character
	Function to create ASCII reference for ROT13 encryption
	First if checks if letter is Upcase A-Z and performs ROT13
	Second if checks if letter is Lowcase a-z and performs ROT13
	If not Upcase or Lowcase A-Z or a-z then retain ordinal of character
	'''
	if ord("A") <= ord(let) <= ord('Z'):
		if ord(let) + 13 <= ord('Z'):
			return ord(let) + 13
		else:
			return ord(let) - ord('Z') + ord('A') +13
	elif ord('a') <= ord(let) <= ord('z'):
		if ord(let) + 13 <= ord('z'):
			return ord(let) + 13
		else:
			return ord(let) - ord('z') + ord('a') + 13
	else:
		return ord(let)


def rot13(string):	
	'''
	This function accepts a string arguement and loops through each character in string
	Each character string is passed to getnumref function for ROT13 encryption
	Each ROT13 encrypted character is appended to list and joined to create string
	'''
	str_container = []
	for let in string:
		str_container.append(chr(getnumref(let)))
	s = ''.join(str_container)
	return s


print(rot13('Zntargvp sebz bhgfvqr arne pbeare'))

