#!/usr/bin/env python3

import numpy as np

def percentages(a, b):
    # what % a represents of b:
    print(f'What % {a} represents of {b}: {b*100/a}')
    # what is the difference in % between a and b:
    print(
        f'what is the difference in % of a between {a} and {b}: {(a-b)*100/a}')
    print(
        f'what is the increment in % from {b} to {a}: {(a-b)*100/b}')
    # what is a double in percentage
    print(
        f'what is a double in percentage, double of {a}: {a*2}, %: {a*2*100/a}')
    # what is an increment in order of magnitude in percentage
    print(
        f'what is an increment in order of magnitude in percentage, {a} one order up: {a*10}, %: {a*10*100/a}')
    for n in range(10):
        print(
            f'what is an increment in order of magnitude in percentage, {a} n:{n} order up: {a*10*n}, %: {a*10*n*100/a}')
    pop_1000 = 3*10**8
    pop_now = 8051765378
    print(f'population increment, 1000 AD: {pop_1000} , now: {pop_now}, {(pop_now-pop_1000)*100/pop_1000}')


if __name__ == '__main__':
    percentages(60, 40)
