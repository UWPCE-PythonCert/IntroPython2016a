language_set = set()

with open('students.txt', 'r') as f:
    for line in f:
        student_info = line.split(':')[1]
        language_list = student_info.split(',')
        for language in language_list:
            language_set.add(language)
print(language_set)
