# Imagine you tell a friend what is 5+5 --> They just shout 10
#--> Print is like that the answer is out there but you can´t save it
#--> If they write it on a letter you can keep it and use it later

#Fundamentals ddifference between print a return

###Print
# Print functon is for humand readable output
# way that the program cmunicates with the user --> print display to the console

print("Hello World")


####Return
#Return statement is a way for a function to comunicate with other parts of the programm
# return gives back a value

####Print
def sum_p(a,b):
    print(a + b) # primer print

result_1 = sum_p(2,4)
print(result_1)


####Print
def sum_r(a,b):
    return a + b 

result_2 = sum_r(2,4)
print(result_2)

#When to use each
#Print when you want the user to see something like a succes message
#Return wzhen you need a value that your programm use later --> A function that calculates with return that amount so another function can process the payment 

#Example

def circle_circumference(radius):
    circumference = 2*3.14159*radius
    return circumference

radius = float(input())

print(f"The circumference of the circke is {circle_circumference(radius)}")
    