### lab-1 FizzBizz program: determine if a list of numbers is 
### divisible by 3/5/both/niether and print out the results

#FIZZBUZZ function
def fizzbuzz(number):

   #if divisible by three or five
    dthr = 0
    dfiv = 0

    # print the number range
    print('The numbers to use from 1 to {0} are'.format(number))

    for n in range(1,number+1):
       # check if numbers are divisible by 3 or 5 or both or niether
         if (n % 3) == 0:
             dthr = 1
             dfiv = 0
             if (n % 5) == 0:
                 dfiv = 1
         elif (n % 5) == 0:
             dfiv = 1
             dthr = 0
         else:
            print(n)
            dthr = 0
            dfiv = 0
         if (dthr == 1 and dfiv ==0):
         	 print('FIZZ')
         if (dthr == 0 and dfiv ==1):
         	 print('BUZZ')
         if (dthr == 1 and dfiv ==1):
         	 print('FIZZBUZZ')
#call the function
fizzbuzz(number=30)