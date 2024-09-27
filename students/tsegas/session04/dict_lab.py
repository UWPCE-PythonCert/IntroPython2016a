# dict_lab.py --- 

my = dict(name='Chris', city='Seattle', cake='chocolate')

print("print the dict",my)
my.pop('cake')
print("print the dict",my)
my['fruit'] = 'mango'
print("print the dict",my)

print("print the dictionary keys",my.keys())
print("print the dictionary values",my.values())

a = "chocolate" in my
print("is chocolate a key in the dictionary?",a)

b = "fruit" in my
print("is Mango a value in the dictionary?",b)

cpy_my = my.copy()
print("print the dict",cpy_my)