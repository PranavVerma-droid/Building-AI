"""
Write a program that prints "I love" followed by one word: the additional word should be 'dogs' with 80% probability, 'cats' with 10% probability, and 'bats' with 10% probability.

Here's an example output:

I love bats
"""


import random

def main():
    prob = random.random()
    if prob < 0.2:
        prob2 = random.random()
        if prob2 < 0.50:
            favourite = "cats"
        else:
            favourite = "bats"
    else:
        favourite = "dogs"
    print("I love " + favourite) 


main()
