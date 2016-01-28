
def main():
    FizzBuzz(100)


def FizzBuzz(number_count):
    ''' This function to print out the numbers from 1 to n, but replace numbers divisible by 3 with "Fizz", numbers
     divisible by 5 with "Buzz". Numbers divisible by both factors should display "FizzBuzz.

    :param number_count: This is the number you want to count up to
    :type number_count: int
    :return: None
    '''

    x = 1
    while x <= number_count: # how can you also use the range function here? 
        # Get the reminder of x when divided by 3 and 5
        check_three = x % 3
        check_five = x % 5

        # Check to see if x is divisible by 3 or 5, and if it isn't, print the number
        if check_five is not 0:
            if check_three is not 0:
                print(x)

        if check_three is 0 and check_five is 0: # can you combine this all into three if/elif/else statments? 
            print("FizzBuzz")
        elif check_three is 0:
            print("Fizz")
        elif check_five is 0:
            print("Buzz")

        x += 1

if __name__ == "__main__":
    main()
