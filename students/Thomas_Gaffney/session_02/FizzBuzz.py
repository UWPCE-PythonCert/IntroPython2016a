def fizzBuzz():
    for i in range(1,101):
    	if((i%3 == 0) and (i%5 !=0)):  print("Fizz") # can you rewrite this so that you don't need the != statements? 
    	elif((i%3 != 0) and (i%5 ==0)):  print("Buzz")
    	elif((i%3 == 0) and (i%5 ==0)):  print("FizzBuzz")
    	else: print(i)

fizzBuzz()
