# Week 2 - Lab #2: MoneyCounting
# Date: Saturday, January 16, 2016
# Student: Chi Kin Ho


def prompt_number_of_coins(prompt):

    """
       This function takes a prompt message of string.
       It prompts the user for the number of coins and returns it.
    """

    # Obtain the number of coins from the user.
    number_of_coins = input(prompt)
    return number_of_coins


def money_counting(pennies, nickels, dimes, quarters):

    """
       This function determines whether a mix of coins can make EXACTLY
       one dollar. Your program should prompt users to enter 4 integers:
       the number of pennies, nickels, dimes, and quarters. If the total
       value of the coins entered is equal to one dollar, the program
       should congratulate users for winning the game. Otherwise, the
       program should display a message indicating whether the amount
       entered was more than or less than a dollar.

    """

    # Check to ensure that pennies, nickels, dimes, and quarters are
    # not negative.
    if pennies < 0 or nickels < 0 or dimes < 0 or quarters < 0:
        # Output an error message.
        print('\nInput Error: Pennies, nickels, dimes, and quarters must be nonnegative.')
        # Return and exit the function.
        return None

    # Calculate the total value based on the number of pennies, nickels,
    # dimes, and quarters.
    total_value = 0.01*pennies + 0.05*nickels + 0.10*dimes + 0.25*quarters
    if total_value == 1: # The total value is $1.00.
        print('\nCongratulations, you win the game!')
    elif total_value > 1: # The total value is greater than $1.00.
        print('\nThe amount entered was more than a dollar.')
    else: # The total value is less than $1.00.
        print('\nThe amount entered was less than a dollar.')


# Prompt the number of pennies from the user.
number_of_pennies = prompt_number_of_coins('Enter the number of pennies: ')
# Prompt the number of nickels from the user.
number_of_nickels = prompt_number_of_coins('Enter the number of nickels: ')
# Prompt the number of dimes from the user.
number_of_dimes = prompt_number_of_coins('Enter the number of dimes: ')
# Prompt the number of quarteres from the user.
number_of_quarters = prompt_number_of_coins('Enter the number of quarters: ')

# Calculate the total value of the coins, and display it on the screen.
money_counting(int(number_of_pennies), int(number_of_nickels),
               int(number_of_dimes), int(number_of_quarters))
