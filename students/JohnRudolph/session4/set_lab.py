cityDic = {'name':'Chris', 'city':'Seattle', 'cake':'chocolate'}

print(cityDic)

cityDic.pop('cake')

print(cityDic)

cityDic['fruit'] = 'Mango'

print(cityDic)

print(cityDic.keys())

print(cityDic.values())

print('cake' in cityDic)

print('Mango' in cityDic.values())

newDic = {}
for item in cityDic:
	newDic[item] = cityDic[item].count('t')

print(newDic)

s2 = set()
s3 = set()
s4 = set()

for i in range(20):
	if i % 2 == 0:
		s2.update([i])
	if i % 3 == 0:
		s3.update([i])
	if i % 4 == 0:
		s4.update([i])

print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

pySet = set()
setString = 'Python'
for let in setString:
	pySet.update([let])

pySet.update(['i'])

print(pySet)

frozen = frozenset(('m', 'a', 'r', 'a','t','h','o','n'))

print(frozen)



