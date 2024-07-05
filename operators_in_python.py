
## Relation Operators. 

"""

a,b = map(int , input("Enter values of a and b:").split())

if a > b : 
    print(f"{a} is greater than {b}")
else : 
    print(f"{b} is greater than {a}")
    
"""

a,b = map(str,input("Enter two names:").split())

if a.isdigit() and b.isdigit(): 
    print(f"Please enter valid names.")
else : 
    if a != b : 
        print(f"Both {a} and {b} are different names.")
    elif a == b : 
        print(f"Both {a} and {b} are same names.")

""" 
## Python calculator using Arithmetic Operators
a,b,c,d = map(int , input("Enter values of a,b,c and d: ").split())

def calculator_to_understand_operators(a,b,c,d) : 
    
    Addition = a + b + c + d 
    Substraction = a - b - c - d 
    Multiplication = a * b * c * d 
    
    list_of_chars = [a,b,c,d]
    list_of_chars.sort()
    
    Division = max(list_of_chars) / min(list_of_chars)
    
    modulus = a//b + c//d 


    return Addition , Substraction , Multiplication , Division , modulus

calculator = calculator_to_understand_operators(a,b,c,d)

print(f"Calculator's Result :\nAddition: {calculator[0]}")
print(f"Substraction: {calculator[1]}")
print(f"Multiplication: {calculator[2]}")
print(f"Division: {calculator[3]}")
print(f"Modulus: {calculator[4]}")
"""
    
    
