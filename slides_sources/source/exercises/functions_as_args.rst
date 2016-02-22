.. _exercise_slicing:


Passing functions to functions
******************************

Goal
----

Practice passing functions as arguments to other functions


Scenario
--------

You are a game designer working on a scoring system.  You have several different categories of weapons: hand weapons, guns, and flower power weapons.  In each of these categories of weapon there is a small, a medium and a large weapon.  Your task is to write a scoring function that takes two arguments and returns an integer which represets the score value of the specified size of the specified weapon.

The first argument to the scoring function is itself a function that represents the cagetory of weapon, be it a hand weapon, a gun or a weapon of the dreaded flower power variety.

The second argument to the scoring function is one of three strings: small, medium or large.  

The score for weapons across the various categories follow the fibonacci scale such that acceptance tests for the scoring function follow the following pattern.  Keep in mind that you need not do any math to get the tests to pass.

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

.. code-block:: python

    def hand_weapon():
        pass	
	
    def gun():
        pass
	
    def flower_power():
        pass
	
    def score(weapon_type, weapon_size):
        pass
