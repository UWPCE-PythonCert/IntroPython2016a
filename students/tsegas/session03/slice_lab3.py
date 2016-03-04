#return a sequence with the first and last 4 items removed, 
#and every other item in between

#original seuqence
seq1 = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d']

#length of the sequence
length = len(seq1)

#print the original sequence
print("original sequence",seq1)

# remove the first 4 items and the last four items from the sequence
seq2 = seq1[4:(length-4)]
print("sequence with first and last 4 items removed",seq2)

n = 1
length2 = len(seq2)
lim = abs(length2/2)
# if sequence length is half the number of original items stop looping
while (length2 > lim):

	seq2.pop(n)
	n=n+1
	if (n > lim):
		print("sequence with every other item in between...",seq2)



