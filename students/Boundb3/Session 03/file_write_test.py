#practice writing to a file

'''
>> with open('test.log', mode='w', encoding='utf-8') as a_file:  ?
...     a_file.write('test succeeded')                            ?
>>> with open('test.log', encoding='utf-8') as a_file:
...     print(a_file.read())
test succeeded
>>> with open('test.log', mode='a', encoding='utf-8') as a_file:  ?
...     a_file.write('and again')
>>> with open('test.log', encoding='utf-8') as a_file:
...     print(a_file.read())
test succeededand again
'''



with open("practicetestfile", mode = "w",encoding='utf-8') as f:
    print(f.tell())
    f.write("try this text\n")
    print(f.tell())
    print("stop")
with open("practicetestfile", mode = "r", encoding='utf-8') as f:
    print(f.tell())
    xdata = (f.read())
    print(f.tell())
    print("finishd read")
    print ("length of data read in f at this time: ",len(xdata))
with open("practicetestfile", mode = "a+",encoding='utf-8') as f:
    print("open in append")
    print(f.tell())
    f.write("I like to try this text again")
    print(f.tell())
    print(f.tell())
    print(f.write("\tThis is last write for the day"))
    print(f.tell())
    f.seek(0)
    print(f.read())
with open("practicetestfile", mode = "r", encoding='utf-8') as f:
    print(f.readline())
    print("hi")
    print(f.readline())

from os.path import exists

print (len("practicetestfile"))
print("does it exist?  true or false \n it is: {} ".format(exists("practicetestfile")))


