input1 = 2
input2 = 123.4567
input3 = 10000

print('File_00{} : {:.2f}, {:.0e}'.format(input1, input2, input3))

t = (1,2,3,4,5)
brackets = '{}'*len(t)

print('The first {}'.format(len(t)), 'numbers are:' + brackets.format(*t))
