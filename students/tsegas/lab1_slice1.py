# return sequence with last and first items changed

seq1 = [4,5,6,7,8,9]

temp = seq1[0]
length = len(seq1)
temp1 = seq1[length-1]

print("original sequence",seq1)

seq1.pop(0)
seq1.pop(length-2)
print("sequence with first and last element removed",seq1)
seq1.append(temp)
seq1.insert(0,temp1)
print("sequence with the first and last items exchanged",seq1)

