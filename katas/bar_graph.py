#!/usr/bin/env python3

import unittest
import numpy as np

# https://www.codewars.com/kata/6444f6b558ed4813e8b70d43/train/python

# You have done some data collection today and you want the data to be well presented by a graph so you have decided to make a quick diagram. 
# Suppose that for this kata your data is presented by an array by their value eg [10,5,3,1,4], then you must present your data as follows:


# for data = [10,5,3,1,4] :
#  ____ ........................ ^ 10
# |    |........................ | 9
# |    |........................ | 8
# |    |........................ | 7
# |    |........................ | 6
# |    | ____ .................. | 5
# |    ||    |............ ____  | 4
# |    ||    | ____ ......|    | | 3
# |    ||    ||    |......|    | | 2
# |    ||    ||    | ____ |    | | 1
# |    ||    ||    ||    ||    | | 0

# GOOD TO KNOW :
#     Each bar is always of width 6.
#     The vertical axis must be surrounded with one space character on each side.
#     No trailing spaces on any line.

#     For this kata we use :
#         the following characters : '_',' ','|','.','^'.
#         some numbers.

#     Return type :
#         Your code must return a character string joined by \n.
#         [] and [0] has different returns "" and " ____  ^ 0"

# CRITERIA :
#     The length of the array is always less than 50.
#     The value of a data is also less than 50 and always positive.

def graph(arr):
    if arr == []:
        return ""
    if arr == [0]:
        return ' ____  ^ 0'
    m = max(arr)
    row = ''
    for j in range(m, -1, -1):
        for val in arr:
            row += (bar(val, j))
        if j == m:
            row += f' ^ {j}\n'
        elif j == 0:
            row += ' | 0'
        else:
            row += f' | {j}\n'
    return row

def bar(value, j):
    if value == j:
        return ' ____ '
    elif value < j:
        return '......'
    else:
        return '|    |'
    

def graph_gpt(arr):
    if not arr:
        return ""
    if arr == [0]:
        return ' ____  ^ 0'
    
    m = max(arr)
    rows = []
    
    for j in range(m, -1, -1):
        row = ''
        for val in arr:
            row += bar(val, j)
        if j == m:
            row += f' ^ {j}'
        elif j == 0:
            row += f' | {j}'
        else:
            row += f' | {j}'
        rows.append(row)
        
    return '\n'.join(rows)

# ############## BEST SOLUTION 

def graph_best(arr):
    if not arr: return ''

    top    = max(arr)+1
    cols   = ( col for h in arr for col in build_bar(h,top) )
    empty  = " " * top
    axis   = "|" * (top-1) + "^"
    nums   = map(str, range(top))
    tilted = [*zip(*cols, empty, axis, empty, nums)]
    out    = '\n'.join(map(''.join, reversed(tilted)))
    return out


def build_bar(h,top):
    fill   = '.' * (top-h-1)
    border = h*'|' + ' ' + fill
    inner  = h*' ' + '_' + fill
    return [border, *(inner for _ in range(4)), border]

# ############# END BEST SOLUTION


sample_test_cases = [
    ([0], ''' ____  ^ 0'''),
    ([1, 3, 5, 4, 1], '''\
............ ____ ............ ^ 5
............|    | ____ ...... | 4
...... ____ |    ||    |...... | 3
......|    ||    ||    |...... | 2
 ____ |    ||    ||    | ____  | 1
|    ||    ||    ||    ||    | | 0'''),

    ([1, 4, 2], '''\
...... ____ ...... ^ 4
......|    |...... | 3
......|    | ____  | 2
 ____ |    ||    | | 1
|    ||    ||    | | 0'''),

    ([10, 5, 3, 1, 4], '''\
 ____ ........................ ^ 10
|    |........................ | 9
|    |........................ | 8
|    |........................ | 7
|    |........................ | 6
|    | ____ .................. | 5
|    ||    |............ ____  | 4
|    ||    | ____ ......|    | | 3
|    ||    ||    |......|    | | 2
|    ||    ||    | ____ |    | | 1
|    ||    ||    ||    ||    | | 0'''),

    ([], ''),
    ([0], ' ____  ^ 0'),
]

class TestGraph(unittest.TestCase):
    def test_graph(self):
        for arr, expected in sample_test_cases:
            self.maxDiff = None
            self.assertEqual(graph(arr), expected)

if __name__ == '__main__':
    unittest.main()
