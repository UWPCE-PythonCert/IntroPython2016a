# Brandon Aleson
# Intro to Python
# 1/27/16
# fizzbuzz

for thing in range(1, 101):
    if (thing % 3 == 0 and thing % 5 == 0):
        print('fizzbuzz')
    elif (thing % 3 == 0):
        print('fizz')
    elif (thing % 5 == 0):
        print('buzz')
    else:
        print(thing)
