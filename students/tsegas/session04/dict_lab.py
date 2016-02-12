# dict_lab.py --- 

my = dict(name='Chris', city='Seattle', cake='chocolate')

print("print the dict",my)
my.pop('cake')
print("print the dict",my)
my['fruit'] = 'mango'
print("print the dict",my)

cpy_my = my.copy()
print("print the dict",cpy_my)