# Write a little script that reads that file
# generates a list of all the languages that have been used.

# Extra credit: track how many students specified each language

language_set = set()
with open('students.txt', 'r') as f:
    pulled_data = f.readlines()
    for line in pulled_data:
        student_languages = line.split(":")[1]
        language_list = student_languages.split(",")
        for language in language_list:
            language_set.add(language)
print(language_set)
