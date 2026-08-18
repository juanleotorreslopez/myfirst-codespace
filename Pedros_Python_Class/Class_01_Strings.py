# Variables -- associate objetcs with a nmae. Objects habe types (belong to classes) 
# Rules for naming variables:
# 1. Names can contain letters, numbers, and underscores.
# 2. Names must start with a letter or an underscore.

#Watch out for: 
#Resevered words (keywords) in Python, which cannot be used as variable names.
#List of reserved words such as: and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, 
# if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield

#Style guide for Python code (PEP 8) 
# Use lowercase letters and underscores for variable names. lowercase_with_underscores
# Use uppercase letters and underscores for Constant variables. UPPERCASE_WITH_UNDERSCORES
# Use CamelCase for class names. CamelCase

#Resources.
# In addition to the official Python documentation, there are many other resources available online for learning Python.
# Some popular ones include:
# Query any object in Python using the help() function. 
#   For example, help(str) will give you information about the str class and its methods.
#help(str)
# An other useful resource is the Python Standard Library documentation, which provides detailed information about the built-in modules and functions available in Python.

#Working with Strings
# Oriented Sequence of characters. 
# Inmutale (cannot be changed) and ordered (the order of the characters is preserved) data type.

#Capitalize the first letter of a string using the capitalize() method.
print("hello world".capitalize()) # Output: Hello world

# prints the string

print("Hello, World!")

# prints the chr at index 3

print("Hello, World"[3])

# prints the last chr

print("Hello, world[-1]")

# print a range 

print("Hello, World"[0:4]) # NOTE: not inclusive of the last index, 4 chrs because python starts at 0

# Index one to the last index

print("Hello, world"[1:]) # NOTE: not inclusive of the last index, 4 chrs because python starts at 0

# EXTENDED SLICING 
# Get every other (2) item in the string.

print("Hello, World"[::2]) # NOTE: not inclusive of the last index, 4 chrs because python starts at 0

# Reverse steps, every other chr

print("Hello, World"[::-2]) # NOTE: not inclusive of the last index, 4 chrs because python starts at 0


# Exercise 1: Make three new strings from the first and last, 
# second and second to last, and third and third to last letters 
# in the string below. Print the three strings.

p = 'redder'
#1 first and last

print(p[0] +p[-1])

#2 second and second to last


print(p[1] +p[-2])

#3 third and third to last


print(p[2] +p[-3])

#String Methods
#Methods are functions that are associated with an object. In Python, strings have many built-in methods that can be used to manipulate and analyze strings. 
# Here are some examples of string methods:

s = "hello world"
#1 Upper Case
print(s.upper()) # Output: HELLO WORLD

#2 Lower Case
print(s.lower()) # Output: hello world

#3 Capitalize the first letter of a string using the capitalize() method.
print(s.capitalize()) # Output: Hello world

#4 Find the index of a substring using the find() method.
print(s.find("o")) # Output: 4

#5 Replace a substring using the replace() method.
print(s.replace("world", "Python")) # Output: hello Python

#6 Split a string into a list of substrings using the split() method.
print(s.split()) # Output: ['hello', 'world']

#7 Strip whitespace from the beginning and end of a string using the strip() method.
s2 = "   hello world   "
print(s2.strip()) # Output: hello world

#8 Join a list of strings into a single string using the join() method.
list_of_strings = ["hello", "world"]
print(" ".join(list_of_strings)) # Output: hello world

#Methods can be chained together, for example:
print(s.upper().replace("WORLD", "PYTHON")) # Output: HELLO PYTHON --> It can reduce clarity, so use it with caution. Except when you are working with, 
#it is also a question of memory and performance, as it can create multiple intermediate strings in memory.


# Exercise 3: Remove the trailing white space in the string below, 
# replace all double spaces with single space, and format to a sentence 
# with proper punctuation. Print the resulting string.

string1 = '  this  is a very badly.  formatted string -  I would  like to make it cleaner\n'

print(string1.strip().replace("  ", " ").replace("i ", "I "))


# Exercise 4: Convert the string below to a list

s = "['apple', 'orange', 'pear', 'cherry']"

list_s = s.split()
print (list_s)
print(type(list_s))


# Exercise 5: Reverse the strings below.      
s1 = 'stressed'
s1_reverse = print(s1[::-1])

s2 = 'drawer'
s2_reverse = print(s2[::-1])
