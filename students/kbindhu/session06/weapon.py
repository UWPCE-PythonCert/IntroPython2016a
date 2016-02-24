def score(weapon_type,weaponsize):
    score_val=weapon_type(weaponsize)
    return score_val


"""hand weapon"""
def hand_weapon(weapon_size):
    if(weapon_size.casefold()=='small'):
        return 1
    elif(weapon_size.casefold()=='medium'):
        return 2
    elif(weapon_size.casefold()=='large'):
        return 3
    else:
        print("invalid size")
"""gun function"""
def gun(weapon_size):
    if(weapon_size.casefold()=='small'):
        return 5
    elif(weapon_size.casefold()=='medium'):
        return 8
    elif(weapon_size.casefold()=='large'):
        return 13
    else:
        print("invalid size")
"""flower_power function"""
def flower_power(weapon_size):
    if(weapon_size.casefold()=='small'):
        return 21
    elif(weapon_size.casefold()=='medium'):
        return 34
    elif(weapon_size.casefold()=='large'):
        return 55
    else:
        print("invalid size")


