#!/usr/bin/python
#fibonacci
def fibonacci(n):
    """Returning base case for recursion ie 0 and 1 case"""
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        """recursively calling fibonacci function for numbers other than 0 and 1
        suppose n=3,the following take place
        fibonacci(3)=fibonacci(1)+fibonacci(2),which breaks
        1+(fibonacci(0)+fibonacci(1)),which is
        1+0+1=2"""
        return(fibonacci(n-2)+fibonacci(n-1))

#print (fibonacci(6))

#lucas function
def lucas(n):
    """Returning base case for recursion ie 0 and 1 case"""
    if(n==0):
        return 2
    elif(n==1):
        return 1
    else:
        """recursively calling fibonacci function for numbers other than 0 and 1
        suppose n=3,the following take place
        lucas(3)=lucas(1)+lucas(2),which breaks
        1+(lucas(0)+lucas(1)),which is
        1+2+1=4"""
        return(lucas(n-2)+lucas(n-1))
#print(lucas(4))

#generiliazed function
def sum_series(reqd,op1=0,op2=1):
    """base values in series are set by optional parameters
    eg if op1 is 0 and op2 is 1 the series will be fibonacci and if op1 and op2 are 2 and 1 respectively series will be lucas
    """
    if(reqd==0):
        return op1
    elif(reqd==1):
        return op2
    else:
        """other vlaues are printed by below statement here function call requires op1 and op2 since they are set from out of
        function"""
        return(sum_series(reqd-2,op1,op2)+sum_series(reqd-1,op1,op2))

#print(sum_series(4,2,1))


#function call
print ("fibonacci  vlaue of 6 is",fibonacci(6))
print("lucas value  of 4 is",lucas(4))
print("value of series  for  (4 3 1 )is",sum_series(4,3,1))
#assertion block
#test for fibonacci series
#testing a passing case for fibonacci
assert fibonacci(6)==8
# testing a failing case for lucas
assert lucas(4)==4
#testing sum series case 
#pass case
assert sum_series(4,3,1)==9
#fail case
assert sum_series(3,3,1)==4
