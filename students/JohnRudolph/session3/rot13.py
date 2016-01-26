
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
			return ord(let) - ord('Z') + ord('A') +12
	elif ord('a') <= ord(let) <= ord('z'):
		if ord(let) + 13 <= ord('z'):
			return ord(let) + 13
		else:
			return ord(let) - ord('z') + ord('a') + 12
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


if __name__ == '__main__':
	print('Zntargvp sebz bhgfvqr arne pbeare', 'ROT13: ', 
		rot13('Zntargvp sebz bhgfvqr arne pbeare'))
	
	print('Blajhkajhds!!! *&^*&^*^POP', 'ROT13: ', 
		rot13('Blajhkajhds!!! *&^*&^*^POP'))

	print('1111 22222 AAAA ZZZZ aaa zzzzz', 'ROT13: ', 
		rot13('1111 22222 AAAA ZZZZ aaa zzzzz'))

	print('abcdefghijklmnopqrstuvwxyz', 'ROT13: ', 
		rot13('abcdefghijklmnopqrstuvwxyz'))

	print('lmnop LMNOP', 'ROT13: ', 
		rot13('lmnop LMNOP'))


