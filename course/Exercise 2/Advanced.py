"""
Building on the previous solution, modify the code so that it finds the route with minimum carbon emissions and prints it out. Again, the program should work for any number of ports. You can assume that the distances between the ports are given in an array of the appropriate size so that the distance between ports i and j is found in D[i][j].

Output Example
PAN AMS CAS NYC HEL 240.1 kg
Tip: Your values might be different, but the formatting should be identical.
"""

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km

D = [
        [0,8943,8019,3652,10545],
        [8943,0,2619,6317,2078],
        [8019,2619,0,5836,4939],
        [3652,6317,5836,0,7825],
        [10545,2078,4939,7825,0]
    ]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)

co2 = 0.020

# DATA BLOCK ENDS

# these variables are initialised to nonsensical values
# your program should determine the correct values for them

smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def permutations(route, ports):
    # write the recursive function here
    # remember to calculate the emissions of the route as the recursion ends
    # and keep track of the route with the lowest emissions

    global smallest
    global bestroute

    if ports == []:
        totalCarbon = 0

        for i in range(0, len(route)-1):
            oldPort = route[i]
            newPort = route[i + 1]

            totalDistance = D[oldPort][newPort]
            totalCarbon = totalCarbon + (totalDistance * co2)

        if totalCarbon < smallest:
            smallest = totalCarbon
            del(bestroute)
            bestroute = route.copy()

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


def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing

    # this will start the recursion 
    permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()
