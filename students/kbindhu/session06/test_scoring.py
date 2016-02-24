#!/usr/bin/env python
from weapon import score
from weapon import hand_weapon
from weapon import gun
from weapon import flower_power



#TESTS
def test_scoring():
    assert score(hand_weapon, 'small') == 1
    assert score(hand_weapon, 'medium') == 2
    assert score(hand_weapon, 'large') == 3
    assert score(gun, 'small') == 5
    assert score(gun, 'medium') == 8
    assert score(gun, 'large') == 13
    assert score(flower_power, 'small') == 21
    assert score(flower_power, 'medium') == 34
    assert score(flower_power, 'large') == 55
