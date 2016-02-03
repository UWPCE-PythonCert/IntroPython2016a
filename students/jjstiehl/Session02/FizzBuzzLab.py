'''
Author: Julie Stiehl
Week 2 Lab#1 FizzBuzz
Notes: this is close but not quite correct
'''
'''
def fizzbuzz(n):
        a = 0 # can you use range here to apply this function to integers between 1 and 100? 
        while a<n:
            print (a)
            a+=1
            if (a%3 == 0) and (a%5 != 0):
                print("Fizz")
            elif(a%5 == 0) and (a%3 !=0):
                print("Buzz")
            elif(a%3 ==0) and (a%5 ==0):
                print("Fizzbuzz")


fizzbuzz(20)
'''


for i in range(1, 101):
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif (i % 3) and (i % 5) == 0:
        print("fizzbuzz")
    else:
        print(i)
