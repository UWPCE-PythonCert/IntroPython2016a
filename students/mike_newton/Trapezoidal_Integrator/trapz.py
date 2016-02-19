import math

#trapz will be passed the function name, a dictionary of arguments/coefficients required for that function,
#a starting point (a) and a stopping point (b).  if no arguments or coefficients are requirements,
#the user will simply pass the word None in the args place when calling trapz.

#each individual function will be responsible for unpacking and using the arguments passed to it from trapz

def trapz(funct, args, a, b):
    N = 100 #number of steps
    step = (b-a)/N #step size

    y = [] #initialize a list of values of y

    for i in range(1,N-1)  #loop through values of x while omitting the first and last points

        x = a + (step * i) #each subsequent x value will be increased by the step size

        y.append(funct(x,args)) # call the desired function and pass it the required arguments and x value

    mid = math.fsum(y) #sum the values of y

    area = step * ((funct(b,args) - funct(a,args))/2 + mid) #find the area under the curve with the trapezoid
                                                            #rule for numerical itnegration

    return area  #return the value of area back to the calling function



def squared(x,args)
    y = x**2
    return y

def quadratic(x, args)
    y = args['A']*x**2 + args['B']*x + args['C']
    return y

make args a dictionary.  user must know what args are required for the function being called
