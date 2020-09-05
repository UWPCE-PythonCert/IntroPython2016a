# Create a wrapper function, safe_input()
# returns None rather rather than raising the exceptions EOFError or KeyboardInterrupt
# when user enters ^C for Keyboard Interrupt, or ^D (^Z on Windows) for End Of File.

def safe_input():
    try:
        input("Type something here")
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        print("Thanks.")
safe_input()
