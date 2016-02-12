import math

#A method to get input from the user and validate that it is an int
def get_integer_input(prompt):
    while True:
        val_is_ok = False
        val = input(prompt)
        try:
            val = int(val)
            val_is_ok = True
        except:
            #Normally too wide an exception scope, but, in this case,
            #anything that isn't explictly an integer is a problem we
            #want to catch.
            print("The quantity entered must be an integer")

        if val_is_ok:
            break
    return val


#Main program
#Opening banner
print("-- The Money Counting Game --")
print("To play, enter the quantity of each type of coin.")
print("If the sum of all the coin you enter totals $1, you win!")

#Play again loop
while True:

    print("\n")
    num_pennies  = get_integer_input("Enter the number of pennies : ")
    num_nickels  = get_integer_input("Enter the number of nickels : ")
    num_dimes    = get_integer_input("Enter the number of dimes   : ")
    num_quarters = get_integer_input("Enter the number of quarters: ")

    total = round((1*num_pennies + 5*num_nickels + 10*num_dimes + 25*num_quarters) / 100, 2)
    delta = round(total - 1.0, 2)

    if total == 1:
        print(" _ _  __          _______ _   _ _   _ ______ _____    _ _ ")
        print("| | | \ \        / /_   _| \ | | \ | |  ____|  __ \  | | |")
        print("| | |  \ \  /\  / /  | | |  \| |  \| | |__  | |__) | | | |")
        print("| | |   \ \/  \/ /   | | | . ` | . ` |  __| |  _  /  | | |")
        print("|_|_|    \  /\  /   _| |_| |\  | |\  | |____| | \ \  |_|_|")
        print("(_|_)     \/  \/   |_____|_| \_|_| \_|______|_|  \_\ (_|_)")
    else:
        print("__     __           _                         __")
        print("\ \   / /          | |                     _ / /")
        print(" \ \_/ /__  _   _  | |     ___  ___  ___  (_) |")
        print("  \   / _ \| | | | | |    / _ \/ __|/ _ \   | |")
        print("   | | (_) | |_| | | |___| (_) \__ \  __/  _| |")
        print("   |_|\___/ \__,_| |______\___/|___/\___| (_) |")
        print("                                             \\_\\")
        print("\n")
        print("Your money totalled: ${0}, which was a difference of ${1} from the goal.".format(total, delta))


    done = False
    while True:
        print("\n")
        play_again = input("Would you like to play again [y/n]? ").lower()
        if play_again not in ['y', 'n']:
            print("Invalid choice. Cmon...it's only 2 keys...you can get this right.")
            print("Now concentrate...")
            continue
        elif play_again in ['n']:
            done = True
            break
        else:
            done = False
            break
    if done :
        break
