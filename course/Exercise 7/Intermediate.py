"""
 Write a program that counts the number of occurrences of "11" in an input sequence of zeros and ones. The input of the program is just the sequence and it should return a single number, which is the number of occurrences of "11". 
"""

def count11(seq):
   # define this function and return the number of occurrences as a number
   counter = 0
   for i in range(0, len(seq) - 1):
       if seq[i] == 1 and seq[i + 1] == 1:
           counter = counter + 1
       else:
           continue
   return counter

print(count11([0, 0, 1, 1, 1, 0])) # this should print 2