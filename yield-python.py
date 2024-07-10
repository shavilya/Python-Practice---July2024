# Using yield , in square pgogram. 

x = 1 
def squares(x) : 
    
    while True : 
        yield x*x 
        x += 1 
        
        
for num in squares(x) : 
    if num > 125  : 
        break 
    print(num)