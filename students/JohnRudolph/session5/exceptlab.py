
def getsafeinput():
    try:
        getinput = input("Input Something\n")
        return getinput
    except (EOFError, KeyboardInterrupt):
        return None

print(getsafeinput())
