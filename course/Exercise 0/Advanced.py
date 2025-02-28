"""
Welcome to your first coding exercise. Please read the instructions in the Intermediate exercise. You can switch between the exercise levels at any time and as many times as you like.

The Advanced exercises differ from the Intermediate ones mainly by the amount of code we provide to start with. In the Intermediate exercises, you are mostly expected to modify a small part of the code, while in the Advanced exercise, you may need to start from scratch.

In all the coding exercises, all the usual tricks apply:

read the problem statement and the comments in the provided code carefully
write code in small bits and run often
feel free to add print statements to see what's going on in the code
click the test button as many times as needed: the test feedback may help you with debugging
Note: if the code template contains functions, it's important to keep their input and output formats the way they are given. The same applies to print statements in case the program is expected produce printed output.
"""

def factorial(n): 
    if n == 0: 
        return 1
    else: 
        return n * factorial(n - 1) 
        
print(factorial(6))