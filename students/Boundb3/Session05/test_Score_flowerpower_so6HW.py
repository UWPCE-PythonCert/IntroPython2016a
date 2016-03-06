'''
This is the test file for HW Score_flowerpower_s06HW

start 2-24-16 B3 - alternative exercise to trapazoid

Goal : Practice passing functions as arguments to other functions
'''


import pytest # I guess this is not necessary

from Score_flowerpower_s06HW import score
from Score_flowerpower_s06HW import hand_weapon
from Score_flowerpower_s06HW import gun
from Score_flowerpower_s06HW import flower_power

def test_scoring():
    assert score(hand_weapon, 'small') == 1
    assert score(hand_weapon, 'medium') == 2
    assert score(hand_weapon, 'large') == 3
def test_scoring2():
    assert score(gun, 'small') == 5
    assert score(gun, 'medium') == 8
    assert score(gun, 'large') == 13
def test_scoring3():
    assert score(flower_power, 'small') == 21
    assert score(flower_power, 'medium') == 34
    assert score(flower_power, 'large') == 55
