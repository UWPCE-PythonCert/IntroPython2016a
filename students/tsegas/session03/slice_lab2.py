#return sequence with every other items removed

#original seuqence
seq1 = [4,5,6,7,8,9]

#length of the sequence
length = len(seq1)

#print the original sequence
print("original sequence",seq1)

n = 1
lim = abs(length/2)
# if sequence length is half the number of original items stop looping
while (length > lim):

	seq1.pop(n)
	n=n+1
	if (n > lim):
		print("sequence with every other item removed...",seq1)



