#!/usr/bin/env python3
import sys
import math
import matplotlib.pyplot as plt
import numpy as np

X_VAL = 1.0

# Helper to make code cleaner
def sin(a):
    return math.sin(a)

# Helper to make code cleaner
def cos(a):
    return math.cos(a)

# Calculates the derivative using finite difference formula
# f'(x) = [f(x+h) - f(x)]/[h]
def approx(h):
    fxh = sin(X_VAL + h)
    fx = sin(X_VAL)
    fdx = (fxh - fx) / h
    return fdx

# Calculate the derivative using cos(x)
def known():
    return cos(X_VAL)

# Helper funtion to calculate the absolute error
# ap: approximate derivative
# k: known derivative 
def absError(ap, k):
    return abs(ap-k)

# Calculates and builds results 
def calculate():
    result = []
    xValues = []
    yValues = []

    for i in range(1, 31):
        h = 2 ** (-1 * i)
        if i < 10:
            hString = "2^-0{}".format(i)
        else:
            hString = "2^-{}".format(i)
        # Approximate Derivative
        ap = approx(h)
        # Known Derivative
        k = known()
        # Absolute Error
        absE = absError(ap, k)
        xValues.append(h)
        yValues.append(absE)
        resDict = {
            'h': hString,
            'x': round(X_VAL, 9),
            'approx': round(ap, 9),
            'known': round(k, 9),
            'absError': round(absE, 9)
        }
        result.append(resDict)

    # Uncomment to plot h vs absolute error values
    # plotResults(xValues, yValues)

    return result

# Helper function to plot h vs absolute error values
def plotResults(xValues, yValues):
    xpoints = np.array(xValues)
    ypoints = np.array(yValues)
    plt.plot(xpoints, ypoints)
    plt.yscale("log")
    plt.xscale("log")
    plt.show()

# Helper function to print the results 
def printResult(result):
    print("|  h  | x | Approx. f'(x) | Known f'(x) | Abs. Error |")
    print("|:---:|:-:|:-------------:|:-----------:|:----------:|")
    for i in result:
        print("|{}|{}|    {}|  {}| {}|".format(i['h'], i['x'], i['approx'], i['known'], i['absError']))

# Is there a minimum value for the magnitude of the error? If such a value exists, how does it compare to √eps (Use the
# Cleve Moler Algorithm to approximate eps.)
def minErrorVEps(result):
    errors = []
    for i in result:
        # Calculate and store the relative error
        errors.append(i['absError'] / i['known'])

    # Find the minimum magnitude of the error
    minError = min(errors)
    # Calculate the machine epsilon and square root it for √eps
    eps = np.finfo(float).eps
    sqrtEPS = math.sqrt(eps)

    print("The minimum value for the magnitude of the error is {}, √eps is {}, the difference between them is {}.".format(minError, sqrtEPS, (abs(minError - sqrtEPS))))

result = calculate()
printResult(result)
minErrorVEps(result)
