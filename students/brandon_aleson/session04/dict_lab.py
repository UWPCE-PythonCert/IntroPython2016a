#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# Brandon Aleson
# Intro to Python
# 1/28/16
# dictionary lab


# 1st series
chrisDict = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}
print(chrisDict)

chrisDict.pop('cake')
print(chrisDict)

chrisDict['fruit'] = 'mango'
print(chrisDict)

print(chrisDict.keys())
print(chrisDict.values())
print('cake' in chrisDict)

chrisValues = chrisDict.values()
print('Chris likes mangoes!') if ('mango' in chrisValues) else print('Chris would prefer not to have a mango thank you very much')


# 2nd series
chrisCopy = {}
for k, v in chrisDict.items():
    chrisCopy[k] = v.count('t')


# 3rd series
s2 = set()
s3 = set()
s4 = set()
for i in range(21):
    if i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)
    if i % 4 == 0:
        s4.add(i)
print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))


# 4th section
ipython = set('python')
ipython.add('i')
marathon = frozenset('marathon')

print(ipython.union(marathon))
print(marathon.union(ipython))
print(ipython.intersection(marathon))
print(marathon.intersection(ipython))
