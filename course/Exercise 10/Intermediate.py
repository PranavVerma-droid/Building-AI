"""
Suppose we have two coins. One is a normal 2 euro coin that comes heads up with 50% probability, and tails up also with 50% probability. The other coin, bought from the magicians' store, has heads on both sides. Good for party tricks and such. It comes heads up with 100% probability.

Suppose now that we choose one of the two coins at random so that either one can be picked with equal probability. The odds that we have the normal coin is thus 1:1.

Let's say the chosen coin keeps landing heads up. How confident can we be that it's the magic coin?

Let's use the naive Bayes method to calculate the odds for the magic coin. We may start with the odds 1:1 since each coin is equally probable to begin with. Each time we flip the coin and it lands heads up, the odds are multiplied by the likelihood ratio which is

r = P(heads | magic) / P(heads | normal) = 1 / 0.5 = 2

Your task: Starting from the odds 1:1 (which is represented as simply the numerical value 1.0), use the naive Bayes method to update the odds for the magic coin after n heads in a row. For example, after three heads (n=3), the odds should be 1 x 2 x 2 x 2 = 8.0.
"""

def flip(n):
    odds = 1.0         # start with 50% chance of the magic coin, which is the same as odds = 1:1
    for i in range(n):
        odds = odds * 2         # edit here to update the odds
    print(odds)

n = 3
flip(n)
