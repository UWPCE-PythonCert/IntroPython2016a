#return a sequence with the middle third, then last third, then the first third in the new order

#original seuqence
seq1 = [1,2,3,4,5,6,7,8,9,10,'a','b']

length = len(seq1)

#print the original sequence
print("original sequence",seq1)

#a third of the length of the list is
third = int(abs(length/3))

# split the sequence into three equal parts
seq2 = seq1[0:(third)]
seq3 = seq1[third:(third*2)]
seq4 = seq1[(third*2):(third*3)]

print("first ..........3rd",seq2)
print("2nd ..........3rd",seq3)
print("3rd ..........3rd",seq4)

# combine the sequence in a different order
nseq = seq3 + seq4 +seq2
print("new sequence:..........",nseq)


