# Admittatily this is not my own work.  I simply could figure it out nor do I under stand how this works yet :)
def main():
    fibonacci(7)

def fibonacci(n):
    x,y = 1,1
    for i in range(n-1):
        x,y = y,x+y
    print(x)

if __name__ == "__main__":
    main()