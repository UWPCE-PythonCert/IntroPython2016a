def main():
    # Prompt user for their guesses
    num_pennies = float(input("Enter number of pennies: "))
    num_nickles = float(input("Enter number of nickles: "))
    num_dimes = float(input("Enter number of dimes: "))
    num_quarter = float(input("Enter number of quarters: "))

    # Add total values based on input
    total_pennies = num_pennies * .01
    total_nickles = num_nickles * .05
    total_dimes = num_dimes * .10
    total_quarters = num_quarter * .25

    # Combine results
    result = total_dimes + total_nickles + total_pennies + total_quarters

    # Check if user hits exactly 1 dollar and if not, provide how much over or under they were
    if result == 1.0:
        print("Congratz for winning the game")
    elif result < 1.0:
        print("Total amount is {} which is under $1.00".format(result))
    else:
        print("Total amount is {} which is above $1.00".format(result))

if __name__ == "__main__":
    main()