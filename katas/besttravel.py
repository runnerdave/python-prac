import itertools
import unittest
# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/python

# John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60]. 
# John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.
# Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible to please Mary and John?

# Example:

# With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].
# The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.
# The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is [55, 58, 60].

# The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1) and ls (list of distances, all distances are positive or zero integers and this list has at least one element). The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise nil, null, None, Nothing, depending on the language. In that case with C, C++, D, Dart, Fortran, F#, Go, Julia, Kotlin, Nim, OCaml, Pascal, Perl, PowerShell, Reason, Rust, Scala, Shell, Swift return -1.
# Examples:

# ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163
# xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, D, Rust, Swift, Go, ...)
# ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228


def choose_bester_sum(t, k, ls):
    try: 
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None

def choose_best_sum(t, k, ls):
    # Get all combinations of k elements from the list ls
    combinations = itertools.combinations(ls, k)

    # Get the sum of each combination and filter out those that exceed t
    valid_combinations = filter(lambda c: sum(c) <= t, combinations)
    
    # Calculate the sum of each valid combination
    valid_sums = []
    for combination in valid_combinations:
        combination_sum = sum(combination)
        valid_sums.append(combination_sum)

    try:
        # Return the maximum valid sum
        return max(valid_sums)
    except ValueError:
        # If there are no valid sums, return None
        return None

    


# without libraries
# 
# def choose_best(t,k,ls):
#     if k == 0: return 0
#     best = -1
#     for i, v in enumerate(ls):
#         if v > t: continue
#         b = choose_best(t - v, k - 1, ls[i+1:])
#         if b < 0: continue
#         b += v
#         if b > best and b <= t:
#             best = b
#     return best

# def choose_best_sum(t, k, ls):
#     c = choose_best(t,k,ls)
#     if c <= 0 : return None
#     return c  

class TestRectangleArea(unittest.TestCase):
    def test_area(self):
        xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
        self.assertAlmostEqual(choose_best_sum(230, 4, xs), 230)
        # self.assertAlmostEqual(choose_best_sum(430, 5, xs), 430)
        # self.assertAlmostEqual(choose_best_sum(430, 8, xs), None)

if __name__ == '__main__':
    unittest.main()
