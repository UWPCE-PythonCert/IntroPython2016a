
def FizzBuzz(n):
    if not isinstance(n, int):
            raise TypeError("FIZZBUZZ: Argument of type {0} is not supported. Only type 'int' is allowed".format(type(n)))
    for i in range(1, n+1):
        if (i % 3 == 0 and i % 5 == 0):
            print('FizzBuzz')
        elif (i % 3 == 0):
            print('Fizz')
        elif (i % 5 == 0):
            print('Buzz')
        else:
            print('{0}'.format(i))


if __name__ == "__main__":
    FizzBuzz(60)
    #FizzBuzz("qwerty")