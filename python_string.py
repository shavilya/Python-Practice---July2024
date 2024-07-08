
""" 
## String slicing.
str1 = "This is simple string inside quotes."

str1_slicing = str1[14:21]
print(f"Output of string slicing : {str1_slicing}")  ## string 

## String Reversed.

str2 = "This str can be reversed?"

print(f"Output: {str2[::-1]}")
str2 = "This str can be reversed?"
 
reversed_str2 = "".join(reversed(str2))  ## Method 2
print(reversed_str2)

"""
## Useful Sting Constants - Built-in Functions 



str3 = "This is a string to test built-in functions"
print(str3.upper())
print(str3.lower())
print(str3.__hash__())
print(str3.endswith('s'))
print(str3.startswith('t'))
print(str3.isdigit())
print(str3.isalpha())
print(str3.swapcase())
print(str3.replace("This" , "It"))
