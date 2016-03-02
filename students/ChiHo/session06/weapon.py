# Weapon Lab
# Student: Chi Kin Ho
# Date: Wednesday, February 17, 2016


def hand_weapon(size):
    if size == 'small':
        return 1
    elif size == 'medium':
        return 2
    else:
        return 3


def gun(size):
    if size == 'small':
        return 5
    elif size == 'medium':
        return 8
    else:
        return 13


def flower_power(size):
    if size == 'small':
        return 21
    elif size == 'medium':
        return 34
    else:
        return 55


def score(weapon_type, weapon_size):
    return weapon_type(weapon_size)

