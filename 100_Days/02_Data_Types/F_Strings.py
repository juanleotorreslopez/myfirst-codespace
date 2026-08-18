#F-Strings 

bmi = 84/1.65 **2
print(bmi)
print(int(bmi)) #ingores the decimal part and returns the integer part of the number. It does not round the number, it simply truncates it.

#round function rounds the number to the nearest integer. If the fractional part of the number is 0.5 or greater, it rounds up to the 
# next integer. If the fractional part is less than 0.5, it rounds down to the previous integer.
print(round(bmi))

print(round(bmi, 2)) #rounds the number to 2 decimal places. The second argument specifies the number of decimal places to round to.


#Asignment Operators --> Assignment operators are used to assign values to variables in Python. They allow you to store data and update it
# as needed. The most common assignment operator is the equal sign (=), which assigns the value on the right to the variable on the left.
# There are also compound assignment operators that combine an operation with assignment, such as +=, -=, *=, and /=, which modify the 
# variable's value based on its current value.

#Score 
score = 0
print(score)  # Output: 0
#User scores point
score += 1 # This is equivalent to score = score + 1
print(score)  # Output: 1

#There is also -=, that remoes a value from the variable, *= that multiplies the variable by a value, and /= that divides the variable 
# by a value.

#F-Strings --> F-strings, or formatted string literals, are a way to embed expressions inside string literals, using a minimal syntax.

print ("Your score is" + str(score)) # This is the old way of formatting strings, using concatenation and type conversion.

#F-strings allow you to include variables and expressions directly within the string, making it more readable and concise. 
# You can create an f-string by prefixing the string with the letter 'f

print(f"Your score is {score}") # This is the new way of formatting strings, using f-strings. The variable score is directly embedded 
#in the string.

score = 0
height = 1.65
is_winning = True

print(f"Your score is {score}, your height is {height}, you are winning is {is_winning}") # This f-string includes multiple variables 
#and expressions, making it easy to create complex strings with dynamic content!