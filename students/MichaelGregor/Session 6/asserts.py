def test_scoring():
    assert score('hand_weapon', 'small') == 1
    assert score('hand_weapon', 'medium') == 2
    assert score('hand_weapon', 'large') == 3
    assert score('gun', 'small') == 5
    assert score('gun', 'medium') == 8
    assert score('gun', 'large') == 13
    assert score('flower_power', 'small') == 21
    assert score('flower_power', 'medium') == 34
    assert score('flower_power', 'large') == 55

def hand_weapon(weapon_size):
    if weapon_size == 'small':
        return 1
    elif weapon_size == 'medium':
        return 2
    elif weapon_size == 'large':
        return 3

def gun(weapon_size):
    if weapon_size == 'small':
        return 5
    elif weapon_size == 'medium':
        return 8
    elif weapon_size == 'large':
        return 13

def flower_power(weapon_size):
    if weapon_size == 'small':
        return 21
    elif weapon_size == 'medium':
        return 34
    elif weapon_size == 'large':
        return 55

def score(weapon_type, weapon_size):

    if weapon_type == 'hand_weapon':
        return hand_weapon(weapon_size)
    elif weapon_type == 'gun':
        return gun(weapon_size)
    elif weapon_type == 'flower_power':
        return flower_power(weapon_size)

