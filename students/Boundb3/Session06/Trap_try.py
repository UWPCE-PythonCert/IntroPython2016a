
def create_range(a,b,n):
    '''
    a = start point
    b = end point
    n = number of intervals to create
    '''
    # create list of x values from a to b
    delta = float(b - a)/n
    print("delta is:", delta, "n:", n)
    return [a+ i * delta  for i in range(n+1)]

x = create_range(1,10,4)
print (x)

my_vals2see = [1,2,3,4,5,6]
print(my_vals2see[1:-1])