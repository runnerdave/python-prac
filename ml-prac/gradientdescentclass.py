#!/usr/bin/env python3
from typing import Callable

class GradientDescent:
    def __init__(self, precision: float = 0.000001):
        self.precision = precision

    def findLocalMinimum(self, f: Callable[[float], float], initialX: float) -> float:
        stepCoefficient = 0.1
        previousStep = 1.0
        currentX = initialX
        previousX = initialX
        previousY = f(previousX)
        iter = 100

        currentX += stepCoefficient * previousY

        while previousStep > self.precision and iter > 0:
            iter -= 1
            currentY = f(currentX)
            if currentY > previousY:
                stepCoefficient = -stepCoefficient / 2
            previousX = currentX
            currentX += stepCoefficient * previousY
            previousY = currentY
            previousStep = abs(currentX - previousX)
        return currentX

def main():
    # Define the function f(x) = x^2 + 2x + 1
    f = lambda x: x**2 + 2*x + 1
    
    # Define the function f(x) = x^2 - 4x + 1
    f2 = lambda x: x ** 2 - 4 * x + 1

    # Create a GradientDescent object
    gd = GradientDescent()

    # Find the local minimum of f starting from x=0
    local_min = gd.findLocalMinimum(f, 0.0)

    # Print the result
    print("Local minimum:", local_min)

    # Find the local minimum of f starting from x=0
    local_min = gd.findLocalMinimum(f2, 0.0)

    # Print the result
    print("Local minimum2:", local_min)

if __name__ == '__main__':
  main()