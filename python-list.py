
list1 = ['This' , 'is' , 'a', 'list' ,"list", "is" , "mutable"]


for i in list1 : 
    print(f"{i} is of  {len(i)} alphabets")
    
    
print(f"Unique list elements are : {set(list1)}")

print(f"Length of {list1} is : {len(list1)}")


list2 = [2,3,5,7,4,8,5]

list2.remove(2) # will remove 2 from list2 
print(f"Elements in list2 are : {list2}")


# List Comprehension 

# Write a list comprehension for printing square number of each element in list2 

squared_elements_in_list2 = [ i**2 for i in list2 ]
print(f"Square Numbers of list2 are : {squared_elements_in_list2}")


# Write a program to interchange first and last element of a list2
list2_copy = list2 
list2_copy[0] , list2_copy[-1] = list2[-1] , list2[0]

print(f"List2 after interchanging first-last elemenst : {list2_copy}")


# Ord() - Built-in function 
list3 = ['a','A','b','B']
for i in list3 : 
    ord_value = ord(i)
    print(f"Original element in list2_copy : {i} , After chaning to ORD : {ord_value}")