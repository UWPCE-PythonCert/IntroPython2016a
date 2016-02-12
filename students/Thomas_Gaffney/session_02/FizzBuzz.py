def fizzBuzz():
    for i in range(1,101):
<<<<<<< HEAD
        if((i%3 == 0) and (i%5 ==0)): print("FizzBuzz")
        elif(i%3 == 0):  print("Fizz")
        elif(i%5 == 0):  print("Buzz")
        else: print(i)
=======
    	if((i%3 == 0) and (i%5 !=0)):  print("Fizz") # can you rewrite this so that you don't need the != statements? 
    	elif((i%3 != 0) and (i%5 ==0)):  print("Buzz")
    	elif((i%3 == 0) and (i%5 ==0)):  print("FizzBuzz")
    	else: print(i)
>>>>>>> upstream/master

fizzBuzz()
