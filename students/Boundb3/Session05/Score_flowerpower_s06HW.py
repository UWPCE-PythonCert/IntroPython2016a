"""
start 2-24-16 B3 - alternative exercise to trapazoid

Goal : Practice passing functions as arguments to other functions
Scenario:
--------
You are a game designer working on a scoring system.  You have several different categories of weapons:
hand weapons, guns, and flower power weapons.  In each of these categories of weapon there is a small, a medium and a large weapon.
Your task is to write a scoring function that takes two arguments and returns an integer which represets the score value of the specified size of the specified weapon.

The first argument to the scoring function is itself a function that represents the cagetory of weapon,
be it a hand weapon, a gun or a weapon of the dreaded flower power variety.

The second argument to the scoring function is one of three strings: small, medium or large.

The score for weapons across the various categories follow the fibonacci scale such that acceptance
tests for the scoring function follow the following pattern.

.. code-block:: python

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


Your task is to fill out the following functions.

code-block:: python
#!!!!!! with Rick:  change d to SWITCH in title,
2nd:  add a default value to the switch dict, so default of zero, and then do something with the zero


"""
# b3 notes 2-24-2016
# see python file test_Score_flowerpower_s06HW.py for the assertions for this file.
# test the assertions via the command line in get bash
# test by typing in: py.test
# note: must be in the same directory - this file, __name__ == main, and the test file w assets, and also the git bash command line folder

# later try to simplify the code by having the weapon functions return a call to the fibinochi function???


def hand_weapon(weapon_size):
    d= {"small": 1, "medium": 2, "large": 3} #using switchdict functionality from session06 notes
    score = d.get(weapon_size)
    return score

def gun(weapon_size):
    d= {"small": 5, "medium": 8, "large": 13}
    score = d.get(weapon_size)
    return score

def flower_power(weapon_size):
    d= {"small": 21, "medium": 34, "large": 55}
    score = d.get(weapon_size)
    return score


def score(weapon_type, weapon_size):
    print("weapon_type is" , weapon_type(weapon_size)) #for testing assets to see where it failed
    score_val = weapon_type(weapon_size)
    return score_val

