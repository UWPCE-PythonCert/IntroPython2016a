#!/usr/bin/python
'''
Create a dictionary containing “name”, “city”, and “cake” for “Chris” from “Seattle” who likes “Chocolate”.
Display the dictionary.
Delete the entry for “cake”.
Display the dictionary.
Add an entry for “fruit” with “Mango” and display the dictionary.
Display the dictionary keys.
Display the dictionary values.
Display whether or not “cake” is a key in the dictionary (i.e. False) (now).
Display whether or not “Mango” is a value in the dictionary (i.e. True).
'''
dict = {'Name': 'Chris', 'City': 'Seattle', 'Cake': 'Chocolate'};
print(dict)
dict.pop('Cake')
print(dict)
dict['Fruit']='Mango'
print(dict)
for x in dict.values():
    print(x)

print('Mango' in dict.values())
print('Cake' in dict.keys())


