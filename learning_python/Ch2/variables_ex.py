# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)

# # re-declaring the variable works
f="abc"
print(f)

# # ERROR: variables of different types cannot be combined
print("A string and", 123)
# print("A string and"+ 123)
print("A string and "+ str(123))


# Global vs. local variables in functions
def some_function():
    f="joe"
    print(f)

def my_function():
    global f
    f="Joseph"
    print(f)


some_function()
print(f)
my_function()
print(f)

# del(f)
# print(f)


