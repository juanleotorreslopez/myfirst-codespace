print("Welcome to Pyathon Pizza Deliveries!")
size = input("What size pizza do ypu want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")



#  Goal print final Bill
# Small 15
# Meidum 20
# Large 25
# Pepperponi S +2
# Pepperoni M L
# Cheese +1 


bill = 0

if size  == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25 
else:
    print("You typed the wrong inputs.")
    

if pepperoni == "Y" and size == "S":
    bill += 2
else: 
    bill += 3
    

if extra_cheese == "Y":
    bill += 1

print (f"You'r final bill si {bill}")
    
    
    