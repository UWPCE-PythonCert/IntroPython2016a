

def main():

    myDict = {'name':'Chris',
              'city':'Seattle',
              'cake':'Chocolate'}

    print(myDict)

    myDict.pop('cake')

    print(myDict)

    myDict.update({'fruit':'Mango'})

    print(myDict)
    print(myDict.keys())

    print(myDict.values())

    find = 'cake' in myDict
    print(find)

    find = 'Mango' in myDict
    print(find)

    myDict = {'name':'Chris',
              'city':'Seattle',
              'cake':'Chocolate'}

    newDict = {('name', 'city', 'cake')}
    count = 0
    for key in myDict:
        value = myDict.get(key)
        count = value.count('t')
        newDict.update(key, count)

    print(newDict)




if __name__ == '__main__':
    main()