"""
Write a program that generates 10000 random zeros and ones where the probability of one is p1 and the probability of zero is 1-p1 (hint: np.random.choice([0,1], p=[1-p1, p1], size=10000)), counts the number of occurrences of 5 consecutive ones ("11111") in the sequence, and outputs this number as a return value. Check that for p1 = 2/3, the count is close to 10000 x (2/3)^5 ≈ 1316.9. 
"""


import numpy as np #type: ignore

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.random.choice([0,1], p=[1-p1, p1], size=10000)
    return seq

def count(seq):
    count = 0
    for i in range(0, len(seq) - 4):
        if seq[i] == 1 and seq[i + 1] == 1 and seq[i + 2] == 1 and seq[i + 3] == 1 and seq[i + 4] == 1:
            count = count + 1
        else:
            continue

    return count

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))
