

# Creating a set 

def create_set() : 
    new_set = {1,2,3,4}
    return new_set 

set_created = create_set()
print(f"New set : {set_created}")

def add_elements() : 
    set_created.add(6)
    
    return set_created 

print(f"Added new element to existing set : {add_elements()}")

def remove_element() : 
    set_created.remove(6) 
    
    return set_created 
print(f"Removing the element from set : {remove_element()}")

set_to_clear = set_created 

def clear_set() : 
    set_to_clear.clear()
    print(set_to_clear)

clear_set()

set1 = {1,2,3,4}
set2 = {2,3,5}

def set_union() : 

    
    union_set = set1.union(set2)
    return union_set

print(f"Union Set : {set_union()}")
        
def set_intersection() : 
    intersection_set = set1.intersection(set2)
    return intersection_set
        
print(f"Intersection Set : {set_intersection()}")

def set_difference() : 
    diff_set = set1.difference(set2)
    return diff_set 

print(f"Difference Set : {set_difference()}")