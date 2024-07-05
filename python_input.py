""" 
a = 1    # Method 1. 
b = 2 


a = int(input("Enter value of a:"))  # Method 2. 
b = int(input("Enter value of b:"))
"""

a,b = map(int , input("enter the value of a and b: ").split())   # Method 3. 
print(f"Hello , world !\nAddition of {a} and {b} is {int(a+b)}")




