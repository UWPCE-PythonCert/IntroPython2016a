__author__ = 'ThomasGaffney'
def switchfirstandlast(stringtouse):
	first = stringtouse[0]
	last = stringtouse [-1]
	middle = stringtouse [1:(len(stringtouse)-1)]
	return (last+middle+first)


test = switchfirstandlast('abcdefghijkl')
print(test)

def reversesequence(stringtouse):
	emptystring = ""
	for i in range(len(stringtouse)):
		emptystring = emptystring + stringtouse[-(len(stringtouse)-i-1)]

print(reversesequence('abcdefghijklmnop'))
