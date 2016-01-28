

def switchfirstandlast(stringtouse):
	first = stringtouse[0]
	last = stringtouse [-1]
	middle = stringtouse [1:(len(stringtouse)-1)]
	return (last+middle+first)


print(switchfirstandlast("abcdefghijkl"))

def everyotheritem(stringtouse):
	newstring=""
	for i in range(len(stringtouse)):
		i=i+1
		if (i%2 != 0): newstring = newstring+stringtouse[i-1]
	return newstring

print(everyotheritem("abcdefghijkl"))

def removefirstandlastfour(stringtouse):
	newstring=stringtouse[4:(len(stringtouse)-4)]
	newstring = everyotheritem(newstring)
	return newstring

print(removefirstandlastfour("abcdefghijklmnop"))

def reversesequence(stringtouse):
	newstring = ""
	for i in range(len(stringtouse)):
		newstring = newstring + stringtouse[-(len(stringtouse)-i-1)]
	return newstring

print(reversesequence('abcdefghijklmnop'))
