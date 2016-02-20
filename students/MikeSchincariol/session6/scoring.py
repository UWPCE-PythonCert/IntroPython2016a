def hand_weapon():
    return {'small': 1,
            'medium': 2,
            'large': 3}

def gun():
    return {'small': 5,
            'medium': 8,
            'large': 13}

def flower_power():
    return {'small': 21,
            'medium': 34,
            'large': 55}

def score(weapon_type, weapon_size):
    return weapon_type()[weapon_size]