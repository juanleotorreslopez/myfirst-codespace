###Len Function 
#The Python len() function returns the number of elements in an object such as a list, string, tuple, dictionary, or any collection that
# implements a length property. It is often one of the first functions that new Python developers learn and is foundational to many programming patterns.
# #Using len() avoids the need to manually count elements, making it indispensable for loops, conditionals, and validations.

#STRING
print(len("Hello, World!"))
print(len([1, 2, 3, 4, 5]))

#Type Functiion Type function is used to check the data type of a variable or value in Python. It returns the type of the object passed to it, allowing developers to verify and work with different data types effectively.
print(type("Hello, World!"))  # <class 'str'>
print(type(42))                 # <class 'int'>
print(type(3.14))               # <class 'float'>
print(type(True))                # <class 'bool'>

#Value Error --> ValueError is a built-in exception in Python that occurs when a function receives an argument of the correct type but 
# an inappropriate value. It indicates that the value provided does not meet the expected criteria or constraints for that operation, 
# leading to an error during execution.
#Len(int("abc")) # ValueError: invalid literal for int() with base 10: 'abc'

#print("Number of letters in your name" + len(input("What is your name?"))) # ValueError: can only concatenate str (not "int") to str
#--> The above line raises a ValueError because it attempts to concatenate a string with an integer (the result of len()), which is not 
# allowed in Python. To fix this, you can convert the integer to a string using the str() function:
# the length is the intiger value of the number of letters in the name, so we need to convert it to string using str() function

print("Number of letters in your name" + str(len(input("What is your name?"))))


