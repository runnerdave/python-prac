#!/usr/bin/env python3

import itertools
import unittest
import numpy as np

# https://www.codewars.com/kata/56f78a42f749ba513b00037f/train/python
#
# Probabilities for Sums in Rolling Cubic Dice
# When we throw 2 classical dice (values on each side from 1 to 6) we have 36 (6 * 6) different results.

# We want to know the probability of having the sum of the results equals to 11.
# For that result we have only the combination of 6 and 5. So we will have two events: {5, 6} and {6, 5}

# So the probability for that result will be:

# P(11, 2) = 2/(6*6) = 1/18    (The two is because we have 2 dice)

# Now, we want to calculate the probability of having the sum equals to 8.
# The combinations for that result will be the following: {4,4}, {3,5}, {5,3}, {2,6}, {6,2} with a total of five combinations.

# P(8, 2) = 5/36

# Things may be more complicated if we have more dices and sum values higher.

# We want to know the probability of having the sum equals to 8 but having 3 dice.

# Now the combinations and corresponding events are:

# {2,3,3}, {3,2,3}, {3,3,2}
# {2,2,4}, {2,4,2}, {4,2,2}
# {1,3,4}, {1,4,3}, {3,1,4}, {4,1,3}, {3,4,1}, {4,3,1}
# {1,2,5}, {1,5,2}, {2,1,5}, {5,1,2}, {2,5,1}, {5,2,1}
# {1,1,6}, {1,6,1}, {6,1,1}

# A total amount of 21 different combinations

# So the probability is:
# P(8, 3) = 21/(6*6*6) = 0.09722222222222222

# Summarizing the cases we have seen with a function that receives the two arguments

# rolldice_sum_prob(11, 2) == 0.0555555555 # or 1/18

# rolldice_sum_prob(8, 2) ==  0.13888888889# or 5/36

# rolldice_sum_prob(8, 3) == 0.0972222222222  # or 7/72

# And think why we have this result:

# rolldice_sum_prob(22, 3) == 0

# Create the function rolldice_sum_prob() for this calculation.


def rolldice_sum_prob(sum, no_dice):
    # edge cases
    if sum > no_dice*6:
        return 0
    if sum < no_dice:
        return 0
    if no_dice == 1:
        return 1/6

    dice = produce_dice(no_dice)
    combinations = 0  
    if no_dice == 2:
        for _ in range(6):
            print_dice(shift_die(dice, 0))
            print(sum_all_columns(dice))
            matching_indices = [i for i, num in enumerate(sum_all_columns(dice)) if num == sum]
            if matching_indices:
                print(f"Matches found at indices: {matching_indices}")
                combinations += len(matching_indices)
            else:
                print("Match not found")
    else:
        for r in range(no_dice):
            for _ in range(6):
                print_dice(shift_die(dice, r))
                print(sum_all_columns(dice))
                matching_indices = [i for i, num in enumerate(sum_all_columns(dice)) if num == sum]
                if matching_indices:
                    print(f"Matches found at indices: {matching_indices}")
                    combinations += len(matching_indices)
                else:
                    print("Match not found")
        for r in range(no_dice-1):
            for _ in range(6):
                print_dice(shift_die(dice, r+1))
                print(sum_all_columns(dice))
                matching_indices = [i for i, num in enumerate(sum_all_columns(dice)) if num == sum]
                if matching_indices:
                    print(f"Matches found at indices: {matching_indices}")
                    combinations += len(matching_indices)
                else:
                    print("Match not found")
        for r in range(no_dice-2):
            for _ in range(6):
                print_dice(shift_die(dice, r+2))
                print(sum_all_columns(dice))
                matching_indices = [i for i, num in enumerate(sum_all_columns(dice)) if num == sum]
                if matching_indices:
                    print(f"Matches found at indices: {matching_indices}")
                    combinations += len(matching_indices)
                else:
                    print("Match not found")
        for r in range(no_dice-2):
            for _ in range(6):
                shift_die(dice, r+2)
                print_dice(shift_die(dice, r+1))
                print(sum_all_columns(dice))
                matching_indices = [i for i, num in enumerate(sum_all_columns(dice)) if num == sum]
                if matching_indices:
                    print(f"Matches found at indices: {matching_indices}")
                    combinations += len(matching_indices)
                else:
                    print("Match not found")
    print(f'combinations:{combinations}')

    return combinations/(6**no_dice)

def run_combinations(dice, pos):
    combinations = 0 
    for _ in range(6):
        print_dice(shift_die(dice, pos))
        print(sum_all_columns(dice))
        matching_indices = [i for i, num in enumerate(sum_all_columns(dice)) if num == sum]
        if matching_indices:
            print(f"Matches found at indices: {matching_indices}")
            combinations += len(matching_indices)
        else:
            print("Match not found")
    return combinations

# one liner: return sum(dice[i][pos] for i in range(len(dice)))
def sum_column(dice, pos):
    sum = 0
    for i in range(len(dice)):
        sum = sum + dice[i][pos]
    return sum    

def sum_all_columns(dice):
    return [sum_column(dice,i) for i in range(6)]

def shift_die(dice, pos):
    lst = dice[pos]
    shift = [lst[-1]] + lst[:-1]
    dice[pos] = shift
    return dice

def produce_dice(n):
    dice = []
    for _ in range(n):
        die = []
        for j in range(6):
            die.append(j+1)
        dice.append(die)
    return dice

def print_dice(dice):
    for d in dice:
        print(d)

# horrible solution, but it generates code programatically
def increase_nested_loops(n):
    if n <= 0:
        print("Invalid input. Please provide a positive integer.")
        return
    loop_variables = ['i' + str(i+1) for i in range(n)]
    loop_ranges = [f'range({i+1})' for i in range(n)]
    code = f"for {', '.join(loop_variables)} in zip({', '.join(loop_ranges)}):"
    code += "\n" + "    " * n + \
        f"print('This is loop number', {', '.join(loop_variables)})"

    print(code)

    exec(code)


def nested_loops(num_loops):
    # Initialize a list of ranges to use for the loops
    ranges = [range(1, i+1) for i in range(1, num_loops+1)]
    # Use itertools.product to generate all possible combinations of values
    for combination in itertools.product(*ranges):
        print(combination)

# TESTS


class TestKata(unittest.TestCase):
    tests = [
        # [[22, 3], 0],
        # [[2, 3], 0],
        # [[6, 1], 1/6],
        # [[11, 2], 1/18],
        # [[8, 2], 5/36],
        [[8, 3], 7/72],
    ]

    def test_function(self):
        for i, test in enumerate(self.tests):
            self.assertEqual(rolldice_sum_prob(test[0][0], test[0][1]),
                             test[1], f'test {i}, value{test[0]} failed')


if __name__ == '__main__':
    # dice = produce_dice(4)
    # print_dice(dice)
    # print(sum_all_columns(dice))
    # print('---')
    # print(sum_all_columns(dice))
    # print('---')
    # print_dice(shift_die(dice, 0))
    # print(sum_all_columns(dice))
    unittest.main()
