shop_dict = {
    "Icecream" : 6 , 
    "Milk" : 3 , 
    "Dairy Milk Chocolate" : 10 
}

print(f"List all the items in my shop : {shop_dict.keys()}")
print(f"List all the items with quantity in my shop : {shop_dict}")

def add_item() : 
    
    shop_dict['Milkshakes'] = 5 
    
    return shop_dict 

print(f"the shop now has  : {add_item()}")


updated_dict = {}
# Write a program to add 2 items in each category 
def add_2_elements_to_stock() : 

    # Update all values by 2
    for key,val in shop_dict:
        shop_dict[val] += 2

    print(shop_dict)
    

