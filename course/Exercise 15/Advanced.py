"""
You are given an array x_train with multiple input vectors (the "training data") and another array x_test with one more input vector (the "test data"). Find the vector in x_train that is most similar to the vector in x_test. In other words, find the nearest neighbor of the test data point x_test.

The code template gives the function dist to calculate the distance between any two vectors. What you need to add is the implementation of the function nearest that takes the arrays x_train and x_test and prints the index (as an integer between 0, ..., len(x_train)-1) of the nearest neighbor.
"""

import numpy as np

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
def nearest(x_train, x_test):
    nearest = -1
    min_distance = np.Inf
    # add a loop here that goes through all the vectors in x_train and finds the one that
    # is nearest to x_test. return the index (between 0, ..., len(x_train)-1) of the nearest
    # neighbor
    for i in range(len(x_train)):
        current = dist(x_train[i], x_test)
        if current < min_distance:
            min_distance = current
            nearest = i
    print(nearest)

nearest(x_train, x_test)
