# from session 5 notes - play with lesson to get practice with concept

import io

with open('output.txt', 'w') as f:
    for i in range(10):
        f.write("this is line: %i\n"%i)
        f.write("\tI am king\n")

with open("output.txt",mode = "r+") as f:
    count = 0
    for i in range(0,5):
        readfile = f.readline()
        print (readfile)

        #f.seek(2+count) # can make the pointer go where I want and then read line again
        #print (f.read()) #reads the whole file

        count += 2
    print("***that was line {:^20} \n". format(i))
    for i in range(0,2):
        readfile = f.readline()
        print (readfile)

print("boolean: ", f.closed)


import io
f2= io.StringIO()
f2.write("here is a sentence \n and here is another \n another\n another")
f2.seek(5)
f2.read()
stuff = f2.getvalue()
print("stuff is:",stuff)
f2.close()

# this is not working - this was from the file notes in session 5
#import os
#a= os.getcwd()
#b= os.chdir(path)
#c= os.path.abspath()
#d = os.path.relpath()
#print(a)


import pathlib
pth = pathlib.Path("./")
print("this is pathlib.Path('./'): ",pth)
print("this is pth.is_dir():", pth.is_dir())
print("pth.absolute(): ", pth.absolute())
#write a program which prints the full path to all files int he current directory - one per line
for f in pth.iterdir():
    print("this is a file in the directory: ",f)

#write a program that copies a file from a source to a destination
for name in pth.iterdir():
    name = str(name)
    print("this is a file in the directory: ",name)
    if name == "file_to_copy_any_kind_process.xlsx":
        doc_name = "file_to_copy_any_kind_process.xlsx"
        with open(doc_name,"rb") as f:
            data_btyes = f.read()
            print("data_btyes is:", data_btyes)
        with open("newname.xlsx", "wb") as newf: # tried C:\Python_100a\IntroPython2016a\students\Boundb3\Session06\newname.xlsx, but it did not work to this new directory
            newf.write(data_btyes)
            print("copied file to: " ) # was not able to copy to another directory, but did make a copy of the file
    else:
        print("not this one:", name)




try: #This is something else I tried, but it is not working !!!
    p = pathlib.Path('.')
    list(p.glob('**/*.py'))
except Exception as e:
    print(e)

