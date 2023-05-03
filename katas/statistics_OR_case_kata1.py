#!/usr/bin/env python3

import unittest
import numpy as np

# https://www.codewars.com/kata/575eac1f484486d4600000b2/train/python
#
# The purpose of this series is developing understanding of stastical problems in AS and A level maths. 
# Let's get started with a simple concept in statistics: Mutually exclusive events.

# The probability of an OR event is calculated by the following rule:

# P(A || B) = P(A) + P(B) - P(A && B)

# The probability of event A or event B happening is equal to the probability of event A plus the probability 
# of event B minus the probability of event A and event B happening simultaneously.

# Mutually exclusive events are events that cannot happen at the same time. For example, 
# the head and tail results of a toin coss are mutually exclusive because they can't both happen at once. 
# Thus, the above example for a coin toss would look like this:

# P(H || T) = P(H) + P(T) - P(H && T)

# Note that the probaility of tossing a coin and the result being both head and tails is 0.

# P(H || T) = (0.5) + (0.5) - (0) P(H || T) = 1

# Thus the probability of a coin toss result being a heads or a tails is 1, in other words: certain.

# Your task:

# You are going to have to work out the probability of one roll of a die returning two given outcomes, or rolls. 
# Given that dice rolls are mutually exclusive, you will have to implement the above forumala. 
# To make this interesting (this is a coding challenge after all), these dice are not fair and thus the probabilites of receiving each roll is different.

# You will be given a two-dimensional array containing the number each of the results (1-6) of the die 
# and the probability of that roll for example [1 , 0.23] as well as the two rolls for example 1 and 5.

# Given the two roll probabilities to calculate, return the probability of a single roll of the die returning either. 
# If the total probability of the six rolls doesn't add up to one, there is a problem with the die; 
# in this case, return null. Return your result as a string to two decimal places.

# Example below:

# 1 : 1/6
# 2 : 1/6
# 3 : 1/6
# 4 : 1/6
# 5 : 1/6
# 6 : 1/6

# If asked for the rolls 1 and 2 then you would need to sum the probabilities, both 1/6 therefore 2/6 and return this. 
# As above, you will need to return it as a decimal and not a fraction.

def mutually_exclusive(dice, call1, call2):
    if sum(item[1] for item in dice) != 1:
        return None
    prob1 = find_die_weight(dice, call1)
    prob2 = find_die_weight(dice, call2)

    return "{:.2f}".format(prob1 + prob2)

def find_die_weight(pairs, die):
    for pair in pairs:
        if pair[0] == die:
            return pair[1]
    return None

def mutually_exclusive_gpt(dice, call1, call2):
    total_weight = sum(pair[1] for pair in dice)
    if total_weight != 1:
        return None

    prob1 = next((pair[1] for pair in dice if pair[0] == call1), None)
    prob2 = next((pair[1] for pair in dice if pair[0] == call2), None)

    if prob1 is None or prob2 is None:
        return None

    return "{:.2f}".format(prob1 + prob2)

def mutually_exclusive_best(dice, call1, call2):
    dice = dict(dice)
    if abs(sum(dice.values()) - 1) < 1e-12:
        return '%0.2f' % (dice[call1] + dice[call2])

# TESTS
class TestKata(unittest.TestCase):
    tests = [
        [([[3,0.4],[4,0.1],[1,0.01],[2,0.09],[5,0.2],[6,0.1]], 1, 6), None],
        [([[1,0.1],[2,0.14],[3,0.16],[4,0.2],[5,0.15],[6,0.25]], 1, 4), "0.30"],
        [([[1,0.6],[2,0.1001],[3,0.0999],[4,0.1],[5,0.05],[6,0.05]], 3, 4), "0.20"],
        [([[6,0.25],[1,0.1],[3,0.16],[2,0.14],[5,0.15],[4,0.2]],1,6), "0.35"],
        [([[3,0.4],[4,0.1],[1,0.01],[2,0.09],[5,0.2],[6,0.2]],1,6), "0.21"],
    ]

    def test_function(self):
        for i, test in enumerate(self.tests):
            self.assertEqual(mutually_exclusive(test[0][0], test[0][1], test[0][2]),
                             test[1], f'test {i}, value {test[0]} failed')

if __name__ == '__main__':
    unittest.main()
