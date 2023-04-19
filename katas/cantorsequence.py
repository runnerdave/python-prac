#!/usr/bin/env python3

import unittest

# https://www.codewars.com/kata/543b9113def6343e43000875
# Georg Cantor's in one of his proofs used following sequence:

# 1/1 1/2 1/3 1/4 1/5 ...
# 2/1 2/2 2/3 2/4 ...
# 3/1 3/2 3/3 ...
# 4/1 4/2 ...
# 5/1 ...

# There are many ways to order those expressions.

# So sequence is:

# 1/1, 1/2, 2/1, 3/1, 2/2, 1/3, 1/4 ...

# Your task is to return nth element of this sequence.

# Input: n - positive integer (max 268435455)

# Output: string - nth expression of sequence - 'a/b' where a and b are integers.


def cantor_sequence(n):
    """Generate the first nth term of the Cantor sequence."""
    matrix_size = n//2 + 1
    matrix = [[(i+1, j+1) for j in range(matrix_size)]
              for i in range(matrix_size)]
    a = 0
    b = 0
    term = matrix[a][b]
    if n == 1:
        return '1/1'
    while n > 1:
        # step right
        if a == 0 and n > 1:
            b = b + 1
            n = n - 1
        # down and left
        while b > 0 and n > 1:
            b = b - 1
            a = a + 1
            n = n - 1
        # down
        if b == 0 and n > 1:
            a = a + 1
            n = n - 1
        # up and right
        while a > 0 and n > 1:
            b = b + 1
            a = a - 1
            n = n - 1
    term = matrix[a][b]
    return f'{term[0]}/{term[1]}'


def cantor_sequence_without_pairing_function(n):
    """Generate the first nth term of the Cantor sequence."""
    if n == 1:
        return '1/1'
    else:
        k = 1
        while n > k:
            n -= k
            k += 1
        if k % 2 == 0:
            return str(n) + '/' + str(k-n+1)
        else:
            return str(k-n+1) + '/' + str(n)
        
from math import isqrt
def cantor_sequence_with_pairing_function(n):
    """Generate the first nth term of the Cantor sequence."""
    # Cantor's pairing function https://en.wikipedia.org/wiki/Pairing_function#Inverting_the_Cantor_pairing_function]
    r = (-1 + isqrt(8 * n - 7)) // 2
    i = r * (r + 1) // 2
    a, b = n - i, i + (r + 1) - (n - 1)
    return f'{b}/{a}' if r % 2 == 0 else f'{a}/{b}'



class TestCantorSequence(unittest.TestCase):
    def test_seq(self):
        self.assertEqual(cantor_sequence(1), '1/1')
        self.assertEqual(cantor_sequence(2), '1/2')
        self.assertEqual(cantor_sequence(3), '2/1')
        self.assertEqual(cantor_sequence(4), '3/1')
        self.assertEqual(cantor_sequence_with_pairing_function(5), '2/2')
        self.assertEqual(cantor_sequence(6), '1/3')
        self.assertEqual(cantor_sequence(7), '1/4')
        self.assertEqual(cantor_sequence(8), '2/3')
        self.assertEqual(cantor_sequence_with_pairing_function(20), '5/2')


if __name__ == '__main__':
    print(f'term: {cantor_sequence_with_pairing_function(2000333333)}')
    unittest.main()
