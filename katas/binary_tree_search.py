#!/usr/bin/env python3

from __future__ import annotations
import unittest
import numpy as np
from typing import Optional

# https://www.codewars.com/kata/5acc79efc6fde7838a0000a0/train/python
#
# 
#

class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right

def search(n: int, root: Optional[Node]) -> bool:
    """ Determines if a value is in a binary tree (NOT bst) """
    # Your code here!
    if root is None:
        return False
    if root.value == n:
        return True
    elif root.value < n:
        return search(n, root.left)
    else:
        return search(n, root.right)

# TESTS
class TestKata(unittest.TestCase):
    tests = [
        [(666, None), False],
        [(444, Node(666, Node(555), Node(444))), True],
        # [(555, Node(666, Node(555), Node(444))), True],
        [(666, Node(666, Node(555), Node(444))), True],
        [(777, Node(666, Node(555), Node(444))), False],
    ]  

    # "Should work with a complete tree")
    SIZE = 20
    nodes = [Node(i) for i in range(20)]
    
    for i in range(SIZE):
        idx_left, idx_right = 2 * i + 1, 2 * i + 2
        nodes[i].left = nodes[idx_left] if idx_left < SIZE else None
        nodes[i].right = nodes[idx_right] if idx_right < SIZE else None

    def test_function(self):
        for i, test in enumerate(self.tests):
            self.assertEqual(search(test[0][0], test[0][1]),
                             test[1], f'test {i}, value{test[0]} failed')            
    
        self.assertEqual(search(self.SIZE, self.nodes[0]), False)
        
        for i in range(self.SIZE):
            self.assertEqual(search(i, self.nodes[0]), True)

if __name__ == '__main__':
    unittest.main()
