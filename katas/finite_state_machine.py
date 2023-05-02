#!/usr/bin/env python3

import unittest

# https://www.codewars.com/kata/5268acac0d3f019add000203/train/python   
#
# Create a finite automaton that has three states. Finite automatons are the same as finite state machines for our purposes.

# Our simple automaton, accepts the language of A, defined as {0, 1} and should have three states: q1, q2, and q3. Here is the description of the states:
#     q1 is our start state, we begin reading commands from here
#     q2 is our accept state, we return true if this is our last state

# And the transitions:
#     q1 moves to q2 when given a 1, and stays at q1 when given a 0
#     q2 moves to q3 when given a 0, and stays at q2 when given a 1
#     q3 moves to q2 when given a 0 or 1

# The automaton should return whether we end in our accepted state (q2), or not (true/false).

# Your task

# You will have to design your state objects, and how your Automaton handles transitions. Also make sure you set up the three states, q1, q2, and q3 for the myAutomaton instance. 
# The test fixtures will be calling against myAutomaton.

# As an aside, the automaton accepts an array of strings, rather than just numbers, or a number represented as a string, 
# because the language an automaton can accept isn't confined to just numbers. An automaton should be able to accept any 'symbol.'

# Here are some resources on DFAs (the automaton this Kata asks you to create):
#     http://en.wikipedia.org/wiki/Deterministic_finite_automaton
#     http://www.cs.odu.edu/~toida/nerzic/390teched/regular/fa/dfa-definitions.html
#     http://www.cse.chalmers.se/~coquand/AUTOMATA/o2.pdf

# Example

# a = Automaton()
# a.read_commands(["1", "0", "0", "1", "0"])  ==> False

# We make these transitions:
# input: ["1", "0", "0", "1", "0"]

# 1: q1 -> q2
# 0: q2 -> q3
# 0: q3 -> q2
# 1: q2 -> q2
# 0: q2 -> q3

# We end in q3 which is not our accept state, so we return false

class Automaton(object):

    def __init__(self):
        self.states = {
            'q1': self.q1,#start state
            'q2': self.q2,#accept state
            'q3': self.q3
        }
        self.current_state = self.q1

    def q1(self, command):
        if command:
            return self.states['q2']
        return self.states['q1']
    
    def q2(self, command):
        if command:
            return self.states['q2']
        return self.states['q3']

    def q3(self, command):
        return self.states['q2']

    def read_commands(self, commands):
        for step in commands:   
            self.current_state = self.current_state(int(step))
        # Return True if we end in our accept state, False otherwise
        return self.current_state == self.states['q2']
    
class AutomatonGPT(object):

    def __init__(self):
        self.states = {
            'q1': self.q1,
            'q2': self.q2,
            'q3': self.q3
        }
        self.current_state = self.q1
    
    def q1(self, command):
        return self.states['q2'] if command else self.states['q1']
    
    def q2(self, command):
        return self.states['q2'] if command else self.states['q3']

    def q3(self, command):
        return self.states['q2']

    def read_commands(self, commands):
        for step in commands:
            # Call the current state function with the current input
            self.current_state = self.current_state(int(step))
        
        # Return True if we end in our accept state (q2), False otherwise
        return self.current_state == self.states['q2']
    

class AutomatonBest(object):

    def __init__(self):
        self.automata = {('q1', '1'): 'q2', ('q1', '0'): 'q1', 
                         ('q2', '0'): 'q3', ('q2', '1'): 'q2',
                         ('q3', '0'): 'q2', ('q3', '1'): 'q2'}
        self.state = "q1"

    def read_commands(self, commands):
        for c in commands:
            self.state = self.automata[(self.state, c)]
        return self.state=="q2"


my_automaton = Automaton()
my_automaton_gpt = AutomatonGPT()
my_automaton_best = AutomatonBest()

# Do anything necessary to set up your automaton's states, q1, q2, and q3.

# TESTS
class TestKata(unittest.TestCase):
    def test_function(self):
        self.assertEqual(my_automaton.read_commands(["1"]), True)
        self.assertEqual(my_automaton.read_commands(["0"]), False)
        self.assertEqual(my_automaton.read_commands(["1", "0", "0", "1"]), True)
        self.assertEqual(my_automaton.read_commands(['1', '0', '0', '1', '0', '0']), True)

if __name__ == '__main__':
    unittest.main()
