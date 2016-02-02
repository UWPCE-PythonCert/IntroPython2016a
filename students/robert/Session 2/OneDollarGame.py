def OneDollarGame():
       p = int(input("Enter # of pennies: "))
       n = int(input("Enter # of nickels: "))
       d = int(input("Enter # of dimes: "))
       q = int(input("Enter # of quarters: "))
       total = p + 5 * n + 10 * d + 25 * q
       if total == 100:
            print ("Congrats, you won 'One Dollar' Game!")
       elif total > 100:
            print ("Sorry it's more than a Dollar")
       else:
            print ("Sorry it's less than a dollar") 
