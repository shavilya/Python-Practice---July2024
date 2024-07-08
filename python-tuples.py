## Tuples 


tuple1 = (2,3,5,6)
tuple2 = (5,3,6,7,3)


# Counts the number of occurence of a particular element 
print(f"{tuple1.count(2)}")
print(f"{tuple2.count(3)}")


# Concatenation of two tuples 

tuple3 = tuple1 + tuple2 
print(f"New Tuple : {tuple3}")

""" 
tuple3[2] = 5 # This will give error as Tuples are Immutable.
print(tuple3)
"""

for i in tuple3 : 
    print(f"{i} : index of {i} , {tuple3.index(i)}") # will give index of that element in tuple3 
    
    
# Sorting of tuples 
tuple4 = sorted(tuple3)
print(tuple4)

# Use Enumerate 

for i in enumerate(tuple4) : 
    print(f"Key: {i[0]} . Value: {i[1]} , Length of i : {len(i)}")