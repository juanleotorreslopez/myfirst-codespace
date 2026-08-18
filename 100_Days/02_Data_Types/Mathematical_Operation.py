#Mathematical Operations in Python
print("My age" + str(30))

#Addition
print(123 + 456)

#Subtraction
print(7-3)

#Multiplication
print(3*4) # Use the * operator to multiply numbers

#Division
print(10/2) # Use the / operator to divide numbers --> When you divide things you always get a float number. Also if its 4 divided by 2 
#you will get 2.0 and not 2. If you want to get an integer you can use the // operator. 
print(type(10//2)) # be really careful with the // operator because it will round down to the nearest whole number. 
#So if you do 5//3 you will get 1 and not 2. 

#Exponents
print(2**2) # Use the ** operator to raise a number to a power. 2**2 means 2 raised to the power of 2 which is 4.
print(2**3) # 2 raised to the power of 3 which is 8.

#Modulus
print(10%3) # Use the % operator to get the remainder of a division. The reminder is the amount left over after division. 
#10 divided by 3 is 3 with a remainder of 1, so 10%3 is 1.

#PEMADSLR
# Parentheses ()
# Exponents **
# Multiplication *
# Addition +
# Subtraction -
# Left to Right

print(3 * 3 + 3 / 3 - 3) # PEMADSLR --> 3*3 = 9, 3/3 = 1, 9+1-3 = 7

#Get 3 instead of 7
print(3 * (3 + 3) / 3 - 3) # 3+3=6, 3*6=18, 18/3=6, 6-3=3 



