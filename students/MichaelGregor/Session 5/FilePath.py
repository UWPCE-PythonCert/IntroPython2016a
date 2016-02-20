import os

for file in os.listdir():
    print(os.path.abspath(file))

with open('students.txt', 'r') as f:
    file = f.read()

with open('students_copy.txt', 'w') as f:
    f.write(file)

for file in os.listdir():
    print(os.path.abspath(file))