"""
Write a program that uses statistics about the population and fishing industry employment to print out conditional probabilities of each nationality given that the winner works in the fishing industry.

The data is given in lists containing the population and the number of fishers in each country.
Output Example

Denmark 14.32%

...

Sweden 08.45%

Tip: Your values might be different, but the formatting should be identical. 
"""

def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    # write your solution here

    for country, population, fisher in zip(countries, populations, fishers):
        print("%s %.2f%%" % (country, (fisher / total_fishers) * 100)) # modify this to print correct results

main()
