"""
In this exercise you need to list all the possible routes that start from Panama and visit each of the other ports exactly once.

The template code below contains an incomplete permutations function which takes as input a specified route and a list of port names absent from that route. Modify the function so that it prints out all the possible orderings of the ports that always begin with Panama (PAN).

The mathematical term for such orderings is a permutation. Note that your program should work for an input portnames list of any length. The order in which the permutations are printed doesn't matter.

As the output the function should print each permutation on its own row, as one string, with the port names separated by spaces. For this, you can use the join function as follows: print(' '.join([portnames[i] for i in route])).

Output Example
PAN AMS CAS NYC HEL

...

PAN CAS AMS NYC HEL
Tip: Your values might be different, but the formatting should be identical.
"""

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
#portnames = [0, 1, 2, 3, 4]

 
def permutations(route, ports):

    if ports == []:
        print(' '.join([portnames[i] for i in route]))
        return

    for i in ports:
        newRoute = route + [i]
        newPorts = []

        for x in ports:
            if x == i:
                continue
            else:
                newPorts.append(x)

        permutations(newRoute, newPorts)

              

# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))
