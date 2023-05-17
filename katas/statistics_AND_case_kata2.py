#!/usr/bin/env python3

import unittest
import numpy as np

# https://www.codewars.com/kata/576a527ea25aae70b7000c77
#
# In the previous Kata we discussed the OR case.

# We will now discuss the AND case, where rather than calculating the probablility for either of two (or more)
# possible results, we will calculate the probability of receiving all of the viewed outcomes.

# For example, if we want to know the probability of receiving head OR tails in two tosses of a coin,
#  as in the last Kata we add the two probabilities together. However if we want to know the probability
# of receiving head AND tails, in that order, we have to work differently.

# The probability of an AND event is calculated by the following rule:

# P(A ∩ B) = P(A | B) * P(B)
# or
# P(B ∩ A) = P(B | A) * P(A)

# That is, the probability of A and B both occuring is equal to the probability of A given B occuring
# times the probability of B occuring or vice versa. If the events are independent, like in the case of tossing a coin,
# the probability of A occuring if B has occured is equal to the probability of A occuring by itself.
# In this case, the probability can be written as the below:

# P(A ∩ B) = P(A) * P(B)
# or
# P(B ∩ A) = P(B) * P(A)

# Applying to the heads and tails case:

# P(H ∩ T) = 0.5 * 0.5
# or
# P(H ∩ T) = 0.5 * 0.5

# The task:

# You are given a random bag of 10 balls containing 4 colours. Red, Green, Yellow and Blue.
# You will also be given a sequence of 2 balls of any colour e.g. Green and Red or Yellow and Yellow.

# You have to return the probability of pulling a ball at random out of the bag and it
# matching the first colour and then pulling a ball at random out of the bag and it matching the second colour.

# You will be given a boolean value of true or false which indicates whether the balls that is taken out
# in the first draw is replaced in to the bag for the second draw.
# Hint: this will determine whether the events are independent or not.

# You will receive two arrays and a boolean value. The first array contains the colours of the balls
# in the bag and the second contains the colour of the two balls you have to receive.
# As per above the final boolean value will indicate whether the balls are being replaced true or not false.

# Do not mutate your inputs and do not round results.

# e.g. [["y","r","g","b","b","y","r","g","r","r"],["r","b"],false]


def ball_probability(balls):
    bag = balls[0]
    ball1 = balls[1][0]
    ball2 = balls[1][1]
    remove_ball = balls[2]
    prob1 = find_probability(bag, ball1)
    # if false remove first ball from bag
    if not remove_ball and prob1 > 0:
        bag.remove(ball1)
    prob2 = find_probability(bag, ball2)
    return round(prob1 * prob2, 3)


def find_probability(bag, ball):
    counts_weighted = {item: bag.count(item)/len(bag) for item in set(bag)}
    return counts_weighted.get(ball, 0)

def ball_probability_best(balls):
    colors, (first, second), replaced = balls
    first_choice = colors.count(first) / len(colors)
    print(first_choice)
    second_choice = colors.count(second) / len(colors) if replaced else (colors.count(second) - 1 * (first == second)) / (len(colors) - 1)
    print(second_choice)
    return round(first_choice * second_choice, 3)


# TESTS
class TestKata(unittest.TestCase):
    tests = [
        [([["red", "blue", "yellow", "green", "red", "blue", "yellow",
          "green", "red", "blue"], ["red", "blue"], True]), 0.090],
        [([["red", "blue", "yellow", "green", "red", "blue", "yellow",
          "green", "red", "blue"], ["red", "red"], True]), 0.090],
        [([["red", "red", "yellow", "green", "red", "red", "yellow",
          "green", "red", "red"], ["blue", "blue"], True]), 0],
        [([["red", "blue", "yellow", "green", "red", "blue", "yellow",
          "green", "red", "blue"], ["red", "blue"], False]), 0.100],
        [([["red", "blue", "yellow", "green", "red", "blue", "yellow",
          "green", "red", "blue"], ["red", "red"], False]), 0.067],
    ]

    def test_function(self):
        for i, test in enumerate(self.tests):
            print(f'test:{i}')
            self.assertAlmostEqual(first=ball_probability(test[0]),
                                   second=test[1], delta=1e-3, msg=f'test {i}, value {test[0]} failed')


if __name__ == '__main__':
    unittest.main()
