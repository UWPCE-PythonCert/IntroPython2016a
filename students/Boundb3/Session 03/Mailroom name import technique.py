# or compare to a second way to prep the dictionary
objFileName = "C:\Python_100a\IntroPython2016a\students\Boundb3\Textfiles\Mail_List_status_W4.txt"
strData = ""
dicTable = {}

#read in the lines from text file and populate a dictionary.
   # problem *** they are now each strings, not tuple and list for the key and values respectively***

objFile = open(objFileName, "r")
for line in objFile:
 strData = line # readline() reads a line of the data
 lstData = strData.split(":") # divide the data into 2 elements - 1 preped for keys (tuple) and 2nd preped for [list]
 dicTable[lstData[0].strip()] = lstData[1].strip()
objFile.close()

dicTableCopy.update(dicTable) # cant iterate over a dictionary - so this does not work

for strKey, strValue in dicTablecopy.items():
    print ("type of strKey is", type(strKey), strKey)
    nameo = strKey.split(",")
    print ("type of nameo is", type(nameo))
    print(nameo[0],"  ", nameo[1],"   ",nameo[2])


    print ("nameo 0 is",nameo[0].strip('""'),"nameo 1 is", nameo[1].strip('""'), "nameo 2 is ", nameo[2].strip('""'))
    #print(strKey + " / " + strValue + "\t")
    #print("type ofkey",type(strKey))
    print("type ofvalue",type(strValue))



if "Sally, Wood, Ms."  in dicTable.keys(): print("yes we have sally")



