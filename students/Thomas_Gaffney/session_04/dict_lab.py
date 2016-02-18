startdict = {'Name' : "Chris", "City" : "Seattle", "Cake" : "Chocoolate"}

print(startdict['Name'])

startdict.pop('Cake')

print(startdict)

startdict['fruit'] = 'Mango'

print(startdict.keys())
print(startdict.values())
print('cake' in startdict.keys())
print('Mango' in startdict.values())


newdict ={}
for keys in startdict.keys():
    print(keys)
    newdict[keys] = startdict[keys].count('t')+startdict[keys].count('T')

print(newdict)

s2 = set(range(0,21, 2))
s3 = set(range(0,21,3))
s4 = set(range(0,21,4))
print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

pythonset = set(['p', 'y', 't', 'h', 'o', 'n'])
pythonset.update(['i'])
print(pythonset)

frozenset = set(['m','a','r','a','t','h','o','n'])
print(frozenset)

print(pythonset.union(frozenset))
print(pythonset.intersection(frozenset))