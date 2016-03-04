#return sequence with last and first items changed

#original seuqence
seq1 = [4,5,6,7,8,9]

# assign the first element to temp
temp = seq1[0]

#length of the sequence
length = len(seq1)

#assign the lat element to temp1
temp1 = seq1[length-1]

#print the original sequence
print("original sequence",seq1)

#remove the first element
seq1.pop(0)

#remove the last element
seq1.pop(length-2)
print("sequence with first and last element removed",seq1)

#append the first element which was stored in temp
seq1.append(temp)

#insert the last element which was stored in temp1
seq1.insert(0,temp1)
print("sequence with the first and last items exchanged",seq1)

