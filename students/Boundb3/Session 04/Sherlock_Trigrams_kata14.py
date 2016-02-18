#"assignment from session 4 - create a trigram from kata 14:by tom swift
#use text file from sherlock from gutenberg"

#open and count data lines
l=[]
with open("sherlock.txt",mode = "r", encoding= "utf-8") as f:
    lines = sum(1 for _ in f)
    print ("count of lines in the text file is: ", lines)

#clean the data and read into a list (one line at a time)

with open("sherlock.txt",mode = "r", encoding= "utf-8") as f:
    for count in range(1,int(lines/10)): #just took a tenth of the whole thing after running the sherlock_short.txt
        read_data = f.readline().strip()
        read_data = read_data.replace("--"," ")
        read_data = read_data.replace("(","")
        read_data = read_data.replace(")","")
        read_data = read_data.replace(","," ") #changing a comma into a space - to separate when it is split
        #read_data = read_data.replace(".","")
        read_data = read_data.replace("'","")
        read_data = read_data.replace('"',"")
        read_data = read_data.lower()
        #print(read_data) # i dont need this for the big file
        word_list= read_data.split()
        l.extend(word_list)
    print("l is:", l)

# top popular words
popular_word_dict = {}
for item in l:
    if item not in popular_word_dict:
        popular_word_dict[item] = 1 #****not working here
    else:
        popular_word_dict[item] += 1
print ("pop dict is: " ,popular_word_dict)

# print out word and count pairs:
for i in sorted(popular_word_dict):
    print (i, popular_word_dict[i], end=" | ") #but I would like this to be sorted by the value - see below
print("\n***complete\n")

#sort on values to find the most popular 20 words
popular_words = sorted(popular_word_dict,key=popular_word_dict.get,reverse=True) #the keys sorted by value
for i in range (1,20):
    print("top 20 word:", popular_words[i], end = "  |  ")## i lost the word's count so I could see how many counts each of these top words got

print("\n\nsorted pop words", popular_words)

#"THIS IS VERY COOL"
#trying chapter 11 dictionaries page 130 Think Python - create an inverse dictionary (to have a count in the key)
inverse = {}
for k in popular_word_dict:

    val = popular_word_dict[k] #this grabs the value of K (so the count in this case)
    if val not in inverse: #if this is a new count number
        inverse[val] = [k] #input the count number as the key, and assign the value of k (the word) to it
    else:
        inverse[val].append(k) # if the count already has a word, add another word to the count key
print ("*** this is inverse**** \n",inverse)

#sort on the keys to know the range of counts in the file (if you wanted)
s_inverse = sorted(inverse, reverse = True) # this just gives me the keys again, at least we know the values
print ("***sorted inverse***", s_inverse)

#***now we can print the words in the counts for the counts which we want to see (by count)
for k,v in inverse.items():
    if k >= 4:
        print ("count= ", k, "value = ", v, "\n")



#convert the list reference items into a dictionary key and value pair for the Triagrams
list_len= len(l)
d={}
for count in range (1,(list_len-2)):
    k = (l[count]+ " " + l[count+1])
    if k not in d: # a new key entry
        d[k] = l[(count+2)]
    else:
        d[k] = (d[k] + " | " + l[(count+2)]) # for a repeated key, so add the new value item to the key's value

print("d is:",d)

#size check

print(list_len)
dict_len = len(d)
print(dict_len)

#try to print a trigram

def start_first_two_words(word1="of", word2="the"):
    start_words = word1 + " " + word2
    print("starting 2 words are: ", start_words)
    return start_words

def split_two_words(first_two_words):
    w1,w2 = first_two_words.split()
    new_w1 = w2
    return new_w1

def get_w3(two_word_key):

    possible_w3_values = [] #start a list for enumerate
    #print("****the two word key to get values on is:", two_word_key)
    values = d[two_word_key] #get all the values for the key and put it in a variable
    values = values.strip().split("|") # split up the contents of the variable by the pipe i insterted into the dict
    if len(values) == 1:
        return values[0]
    elif len(values) == 0:
        return "game over"
    else: # if the contents are greater than one element, then we need to pick one
        for element in values:
            possible_w3_values.append(element)
        #for i,v in enumerate(possible_w3_values):
        #    print (i,v)
        #choice = None
        max = int(len(possible_w3_values))
        choice = random.randint(0,max-1)
        #choice = int(input("chose which value above to be the next word"))
        w3 = possible_w3_values[choice]
        w3 = w3.strip()

        return w3

#main menu

import random
print("lets start")
input("hit any key to start")

#get first two words
start_words = start_first_two_words()
print("\n start_words")

#try for a few rounds
for i in range (1,1000):
    count += 1
    new_w1 = split_two_words(start_words)
    w3 = get_w3(start_words)
    print(w3, " " , end= "")
    #print("to here")
    next_two_words = new_w1 +" "+  w3
    #print("got these two words donw", next_two_words)
    start_words = next_two_words
    if count % 20 == 0: print("\n")

print("over; ran out of words")



'''
count = 0
for word in read_data:
    count +=1

print (count)
'''
