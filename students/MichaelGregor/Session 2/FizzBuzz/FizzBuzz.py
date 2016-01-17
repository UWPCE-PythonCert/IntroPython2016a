number_count = 20
x=1
while x <= number_count:
    # Get the reminder of x when divided by 3 and 5
    check_three = x%3
    check_five = x%5

    # Check to see if x is divisable by 3 and 5, and if it isn't, print the number
    if check_five is not 0:
        if check_three is not 0:
            print(x)
    
    if check_three is 0 and check_five is 0:
        print("FizzBuzz")
    elif check_three is 0:
        print("Fizz")
    elif check_five is 0:
        print("Buzz")

    x+=1