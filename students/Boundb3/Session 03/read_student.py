'''
create a file that opens and reads the student language file.
 1. create a list of all the languages that have been used
 2. if possible,can keep track of how many languages the students have each


'''

import os



# f = open("C:\Python_100a\IntroPython2016a\students\Boundb3\Textfiles\students.txt", "r"):


language_set = set ()

with open('C:\Python_100a\IntroPython2016a\students\Boundb3\Textfiles\students.txt', 'r') as f:
    for line in f:
        student_lang = line.rsplit(':')[1]
        language_list = student_lang.split(",")
        for language in language_list:
            language = language.strip("\n")
            language_set.add(language)

print(language_set)
print(len(language_set))

'''
# we can take out zero length lengths,
'''





