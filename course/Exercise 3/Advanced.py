"""
The following program starts at a random position and keeps going to the right until Venla can no longer go up. However, perhaps the mountain is a bit rugged which means it's necessary to look a bit further ahead.

Edit the program so that Venla doesn't stop climbing as long as she can go up by moving up to five steps either left or right. If there are multiple choices within five steps that go up, any one of them is good. To check how your climbing algorithm works in action, you can plot the results of your hill climbing using the Plot button. As a reminder, the summit will be marked with a blue triangle.
"""

import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 

w = [.05, random.random()/3, random.random()/3]
h = [1.+math.sin(1+x/.6)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False

    # edit here
    while not summit:         
        if h[x + 1] > h[x]:
            x = x + 1         # right is higher, go there
            summit = False    # and keep going
        elif h[x - 1] > h[x]:
            x = x - 1         # left is higher, go there
            summit = False    # and keep going
        else:
            # Check up to 5 steps right
            for i in range(1, 6):
                if x + i < len(h) and h[x + i] > h[x]:
                    x = x + i
                    summit = False    # found a way up, keep going
                    break
            # If no higher position right, check up to 5 steps left
            else:
                for i in range(1, 6):
                    if x - i >= 0 and h[x - i] > h[x]:
                        x = x - i
                        summit = False    # found a way up, keep going
                        break
                else:
                    summit = True     # stop unless there's a way up
    return x


def main(h):
    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x
    
main(h)
