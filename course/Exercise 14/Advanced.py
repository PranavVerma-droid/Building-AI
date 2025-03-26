"""
Write a program that reads data about one set of cabins (training data), estimates linear regression coefficients based on it, then reads data about another set of cabins (test data), and predicts the prices in it. Note that both data sets contain the actual prices, but the program should ignore the prices in the second set. They are given only for comparison.

The contents of the sets are as follows.

training data

size 	size of the sauna 	distance to water 	number of indoor bathrooms 	proximity of neighbors 	actual price
25 	2 	50 	1 	500 	127900
39 	3 	10 	1 	1000 	222100
13 	2 	13 	1 	1000 	143750
82 	5 	20 	2 	120 	268000
130 	6 	10 	2 	600 	460700
115 	6 	10 	1 	550 	407000

test data

size 	size of the sauna 	distance to water 	number of indoor bathrooms 	proximity of neighbors 	actual price
36 	3 	15 	1 	850 	196000
75 	5 	18 	2 	540 	290000

You can read the data into the program the same way as in the previous exercise.

You should then separate the feature and price data that you have just read from the file into two separate arrays names x_train and y_train, so that you can use them as argument to np.linalg.lstsq.

The program should work even if the number of features used to describe the cabins differs from five (as long as the same number of features are given in each file).

The output should be the set of coefficients for the linear regression and the predicted prices for the second set of cabins.
"""


import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
    
    # Please write your code inside this function
    train_data = np.genfromtxt(StringIO(train_string), skip_header=0)

    x_train = train_data[:, :-1]  # all columns except the last
    y_train = train_data[:, -1] 
     
    # fit a linear regression model to the data and get the coefficients
    c = np.linalg.lstsq(x_train, y_train, rcond=-1)[0]

    # read in the test data and separate x_test from it
    test_data = np.genfromtxt(StringIO(test_string), skip_header=0)
    x_test = test_data[:, :-1]

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)


main()
