#!/usr/bin/python

"""remove comments to run the function"""
#part1 of grid excercise

def grid_part1():
    plus=  '+'
    minus='-'
    bar='|'
    for i in range(3):
        """below prints +----+----+"""
        print(plus+4*minus+plus+4*minus+plus)
        if(i==2):
            """this break is make sure only +----+ will be printed last doesnt need the |---|---|"""
            break
        for j in range(4):
            """print |    |    | four times"""
            print(bar+4*" "+bar+4*" "+bar)

#call function for testing
#grid_part1()

#Part2 of grid exercise generalized function

def grid_part2(n):
    plus=  '+'
    minus='-'
    bar='|'
    mult=n//2
    for i in range(3):
        """below prints +----+----+"""
        print(plus+mult*minus+plus+mult*minus+plus)
        if(i==2):
            """this break is make sure only +----+ will be printed last doesnt need the |---|---|"""
            break
        for j in range(mult):
            """print |    |    | mult times"""
            print(bar+mult*" "+bar+mult*" "+bar)

#call function for testing
#grid_part2(15)


#part3 of grid execise
# my comments assume grid(3,4) ie 3 rows and 4 columns
def grid_part3(rows,columns):
    plus=  '+'
    minus='-'
    bar='|'
    for l in range(rows):
        for i in range(rows):
            """ print (+ and  columns*-)eg:grid(3,4)  below
            loop prints "+---- "for 3 times (rows) ie +----+----+----+"""
            print(plus+columns*minus,end='')
        print(plus)
        """below loop prints bar followed by spaces*no of columns.
        Inner j loop prints 'bar followed by 4 spaces(columns)
        outerloop with k iterator print tha bar  folllowed by 4 spaces it for no of rows"""
        for k in range(columns):
            for j in range (rows+1):
                print(bar+columns*" ",end='')
                """newline"""
            print() 
            """ below loop print last  line of grid which is a +- pattern"""
    for m in range(rows):
        print(plus+columns*minus,end='')
    print(plus)


#call for function
#grid_part3(5,3)
