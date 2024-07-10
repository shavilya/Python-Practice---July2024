## Functions in Python 


""" 
Some benefits of using functions
1. Increase code readability 
2. Increase code reusability 
"""

""" 
# Simple Function 

def simpleFunction() : 
    print("This is a function")

simpleFunction()
"""

""" 
# Function with parameters 

a,b = 10,20 

def sum(a,b) : 
    return a+b 

print(f"Sum of {a} and {b} is {sum(a,b)}")
"""

""" 
# Python function arguments 

def evenOdd(x) : 
    if x%2 == 0 : 
        print("Even")
    else : 
        print("Odd")
        
evenOdd(2) 
"""
""" 
# Recursive function in python 

# Write a function to print factorial
def factorial(n) : 
    if n == 0 : 
        return 1 
    else : 
        return n * factorial(n-1)

print(factorial(4))
"""

# Write a function to swap x and y values. 

x,y = 0,1
print(f"values before swapping: {x,y}")
def swapValues(x,y) : 
    x,y = y,x 
    return x,y 

values_after = swapValues(x,y) 

print(f"values after swapping : {values_after}")    


















