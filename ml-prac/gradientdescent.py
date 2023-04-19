#!/usr/bin/env python3

import sys

def gradient_descent(function, initial_point, learning_rate=0.1, threshold=1e-5, max_iterations=1000):
    """
    Executes the gradient descent algorithm on a given function to find its minimum point.
    :param function: The function to find the minimum of.
    :param initial_point: The starting point for the algorithm.
    :param learning_rate: The learning rate or step size for each iteration.
    :param threshold: The threshold value for the minimum difference between two consecutive points.
    :param max_iterations: The maximum number of iterations to perform.
    :return: The minimum point of the function.
    """
    point = initial_point
    iteration = 0
    while True:
        gradient = function(point)
        print(f'point: {point}, gradient {gradient}')
        new_point = point - learning_rate * gradient
        if abs(new_point - point) < threshold:
            break
        point = new_point
        iteration += 1
        if iteration >= max_iterations:
            break
    return point

def gradient_descent_beta(function, initial_x, learning_rate=0.1, threshold=1e-5, max_iterations=1000):
   previous_step = 1.0
   previous_y = function(initial_x)
   print (f'previous_y:{previous_y}')
   previous_x = initial_x
   next_x = initial_x + previous_y*learning_rate
   print (f'next_x:{next_x}')
   i = 0
   while previous_step > threshold and i < max_iterations:
      i += 1
      next_y = function(next_x)
      if next_y > previous_y:
         learning_rate = -learning_rate/2
      previous_y = next_y
      previous_x = next_x
      next_x += previous_y*learning_rate
      previous_step = abs(next_x - previous_x)
      print (f'i:{i}, next_y:{next_y}, next_x:{next_x}, learning_rate:{learning_rate}')

   return next_x

def f(x):
    return x ** 2 - 4 * x + 3

def f2(x):
    return x ** 2 - 2 * x - 3


# Define a main() function that prints a little greeting.
def main():
  minimum_point = gradient_descent_beta(f2, 1.5)
  print("Minimum point found at:", minimum_point)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()