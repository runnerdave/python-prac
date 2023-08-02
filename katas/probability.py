#!/usr/bin/env python3

import unittest
import numpy as np
import math

# https://www.codewars.com/kata/5708ccb0fe2d01677c000565/train/python

# Mean, Variance and Standard Deviation of a Probability Distribution for Discrete Variables.

# We have a distribution of probability of a discrete variable (it may have only integer values)

# x       P(x)
# 0       0.125
# 1       0.375
# 2       0.375
# 3       0.125
# Total = 1.000   # The sum of the probabilities for all the possible values should be one (=1)

# The mean, μ, of the values of x is:

# https://imgur.com/EbDq0XT

# For our example

# μ = 0*0.125 + 1*0.375 + 2*0.375 + 3*0.125 = 1.5

# The variance, σ² is:

# https://imgur.com/vMyeQEn

# For our example :

# σ² = 0.75

# The standard deviation, σ is:

# https://imgur.com/mg801Vq

# Finally, for our example:

# σ = 0.8660254037844386

# Make the function stats_disc_distr() that receives a 2D array. Each internal array will have a pair of values: the first one, the value of the variable x and the second one its correspondent probability, P(x).

# For the example given above:

# stats_disc_distr([[0, 0.125], [1, 0.375], [2, 0.375], [3, 0.125]]) == [1.5, 0.75, 0.8660254037844386]

# The function should check also if it is a valid distribution.

# If the sum of the probabilities is different than 1, the function should output an alert.

# stats_disc_distr([[0, 0.425], [1, 0.375], [2, 0.375], [3, 0.125]]) == "It's not a valid distribution"

# If one of the values of x is not an integer, the function will give a specific alert:

# stats_disc_distr([[0.1, 0.425], [1.1, 0.375], [2, 0.375], [3, 0.125]]) == "All the variable values should be integers"

# If the distribution has both problems will output another specific alert:

# stats_disc_distr([[0.1, 0.425], [1.1, 0.375], [2, 0.375], [3, 0.125]]) == "It's not a valid distribution and furthermore, one or more variable value are not integers"

# But if a value is a float with its decimal part equals to 0 will proceed without inconveniences, (if the sum of probabilities is 1:

# stats_disc_distr([[0.0, 0.125], [1.0, 0.375], [2.0, 0.375], [3, 0.125]]) == [1.5, 0.75, 0.8660254037844386]

# The 2Darray will not have any strings.


def stats_disc_distr(distrib):
    # your awesome code here
    mean, var, std_dev = 0, 0, 0
    epsilon = 1e-15
    error = ""

    valid = 0
    for k, v in distrib:
        if int(k) != k:
            error = "All the variable values should be integers"
        valid += v
    if valid != 1 and error != "":
        error = "It's not a valid distribution and furthermore, one or more variable value are not integers"
    elif np.abs(1-valid) > epsilon and error == "":
        error = "It's not a valid distribution"

    if error != "":
        return error

    for p in distrib:
        mean += p[0] * p[1]

    for p in distrib:
        var += (p[0]-mean)**2*p[1]

    std_dev = math.sqrt(var)

    return [mean, var, std_dev]  # or alert messages


def stats_disc_distr_chatgpt(distrib):
    if not np.isclose(sum(p[1] for p in distrib), 1):
        error = "It's not a valid distribution"
        if any(not isinstance(p[0], int) for p in distrib):
            error += " and furthermore, one or more variable value are not integers"
        return error

    if any(not isinstance(p[0], (int, float)) or isinstance(p[0], float) and not p[0].is_integer() for p in distrib):
        return "All the variable values should be integers"

    mean = np.average([p[0] for p in distrib], weights=[p[1] for p in distrib])
    var = np.average([(p[0]-mean)**2 for p in distrib], weights=[p[1] for p in distrib])
    std_dev = np.sqrt(var)

    return [mean, var, std_dev]

## BEST SOLUTION FROM CODEWARS

def stats_disc_distr_best(distrib):
    err = check_errors(distrib)
    if not err:
        mean = sum(x[0] * x[1] for x in distrib)
        var = sum((x[0] - mean) ** 2 * x[1] for x in distrib)
        std_dev = var ** 0.5
    return [mean, var, std_dev] if not err else err

def check_errors(distrib):
    errors = 0
    if not isclose(sum(x[1] for x in distrib), 1):
        errors += 1
    if not all(isinstance(x[0], int) for x in distrib):
        errors += 2
    if errors > 0:
        return {1: "It's not a valid distribution", 2: "All the variable values should be integers",
        3: "It's not a valid distribution and furthermore, one or more variable value are not integers"}[errors]

def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

# TESTS

def assertFuzzyEquals(actual, expected, msg=""):
    merr = 1e-8  # max error
    if expected == 0:
        inrange = math.fabs(actual) <= merr
    else:
        inrange = math.fabs((actual - expected) / expected) <= merr
    if msg == "":
        msg = "Expected value near {:.8f}, but got {:.8f}"
        msg = msg.format(expected, actual)
    return (inrange == msg)


class TestStats(unittest.TestCase):
    def test_function(self):
        distrib = [[0, 0.125], [1, 0.375], [2, 0.375], [3, 0.125]]
        res = stats_disc_distr_chatgpt(distrib)
        result = [1.5, 0.75, 0.8660254037844386]
        for i in range(len(result)):
            assertFuzzyEquals(result[i], res[i])

        distrib = [[0, 0.425], [1, 0.375], [2, 0.375], [3, 0.125]]
        res = stats_disc_distr_chatgpt(distrib)
        result = "It's not a valid distribution"
        self.assertEqual(res, result)

        distrib = [[0.1, 0.125], [1.1, 0.375], [2, 0.375], [3, 0.125]]
        res = stats_disc_distr_chatgpt(distrib)
        result = "All the variable values should be integers"
        self.assertEqual(res, result)

        distrib = [[0.1, 0.425], [1.1, 0.375], [2, 0.375], [3, 0.125]]
        res = stats_disc_distr(distrib)
        result = "It's not a valid distribution and furthermore, one or more variable value are not integers"
        self.assertEqual(res, result)

        distrib = [[0.0, 0.125], [1.0, 0.375], [2.0, 0.375], [3, 0.125]]
        res = stats_disc_distr_chatgpt(distrib)
        result = [1.5, 0.75, 0.8660254037844386]
        self.assertEqual(res, result)

        distrib = [[4, 0.0001], [5, 0.0004], [6, 0.001], [7, 0.002], [8, 0.0035], [9, 0.0056], [10, 0.0084], [11, 0.012], [12, 0.0165], [13, 0.022], [14, 0.0282], [15, 0.0348], [16, 0.0415], [17, 0.048], [18, 0.054], [19, 0.0592], [20, 0.0633], [21, 0.066], [22, 0.067], [23, 0.066], [24, 0.0633], [25, 0.0592], [26, 0.054], [27, 0.048], [28, 0.0415], [29, 0.0348], [30, 0.0282], [31, 0.022], [32, 0.0165], [33, 0.012], [34, 0.0084], [35, 0.0056], [36, 0.0035], [37, 0.002], [38, 0.001], [39, 0.0004], [40, 0.0001]]
        res = stats_disc_distr_chatgpt(distrib)
        result = [22.000000000000004, 33.0, 5.744562646538029]
        for i in range(len(result)):
            assertFuzzyEquals(result[i], res[i])

        distrib = [[5, 3.125e-07], [6, 1.5625e-06], [7, 4.6875e-06], [8, 1.09375e-05], [9, 2.1875e-05], [10, 3.9375e-05], [11, 6.5625e-05], [12, 0.000103125], [13, 0.0001546875], [14, 0.0002234375], [15, 0.0003128125], [16, 0.0004265625], [17, 0.00056875], [18, 0.00074375], [19, 0.00095625], [20, 0.00121125], [21, 0.0015140625], [22, 0.0018703125], [23, 0.0022859375], [24, 0.0027671875], [25, 0.0033190625], [26, 0.0039453125], [27, 0.0046484375], [28, 0.0054296875], [29, 0.0062890625], [30, 0.0072253125], [31, 0.0082359375], [32, 0.0093171875], [33, 0.0104640625], [34, 0.0116703125], [35, 0.0129284375], [36, 0.0142296875], [37, 0.0155640625], [38, 0.0169203125], [39, 0.0182859375], [40, 0.0196471875], [41, 0.0209890625], [42, 0.0222953125], [43, 0.0235484375], [44, 0.0247296875], [45, 0.0258221875], [46, 0.0268109375], [47, 0.0276828125], [48, 0.0284265625], [49, 0.0290328125], [50, 0.0294940625], [51, 0.0298046875], [52, 0.0299609375], [53, 0.0299609375], [54, 0.0298046875], [55, 0.0294940625], [56, 0.0290328125], [57, 0.0284265625], [58, 0.0276828125], [59, 0.0268109375], [60, 0.0258221875], [61, 0.0247296875], [62, 0.0235484375], [63, 0.0222953125], [64, 0.0209890625], [65, 0.0196471875], [66, 0.0182859375], [67, 0.0169203125], [68, 0.0155640625], [69, 0.0142296875], [70, 0.0129284375], [71, 0.0116703125], [72, 0.0104640625], [73, 0.0093171875], [74, 0.0082359375], [75, 0.0072253125], [76, 0.0062890625], [77, 0.0054296875], [78, 0.0046484375], [79, 0.0039453125], [80, 0.0033190625], [81, 0.0027671875], [82, 0.0022859375], [83, 0.0018703125], [84, 0.0015140625], [85, 0.00121125], [86, 0.00095625], [87, 0.00074375], [88, 0.00056875], [89, 0.0004265625], [90, 0.0003128125], [91, 0.0002234375], [92, 0.0001546875], [93, 0.000103125], [94, 6.5625e-05], [95, 3.9375e-05], [96, 2.1875e-05], [97, 1.09375e-05], [98, 4.6875e-06], [99, 1.5625e-06], [100, 3.125e-07]]
        res = stats_disc_distr_chatgpt(distrib)
        result = [52.500000000000014, 166.24999999999994, 12.893796958227625]
        for i in range(len(result)):
            assertFuzzyEquals(result[i], res[i])


if __name__ == '__main__':
    unittest.main()
