

def countdown(n):
    if n < 0:
        print("plastoff")
    else:
        print(n)
        countdown(n-1)
    return n

a=countdown(4)
print ("you started the countdown with {} ".format(a))
