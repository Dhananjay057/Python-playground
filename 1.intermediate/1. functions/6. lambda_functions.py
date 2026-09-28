""" 
lambda functions or anonymous functions - function without a name
"""

def multiply(x):
    return x*2

print(multiply(5))

print((lambda x:x*2)(6))

myList = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x:x%2==0,myList))) # Filters the value to select from original

print(list(map(lambda x:x*2,myList))) # Maps changes the value to new value and returns a new list

print([x for x in myList if x%2==0]) # List comprehension

"""Lambda function was used earlier since it came earlier, 
after that list comprehension was used since it is more readable and faster than lambda function."""