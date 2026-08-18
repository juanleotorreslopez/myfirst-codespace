#elif more conditionals 
# if condition1:
#    do A
# elif condition 2:
#    do B
# else: 
#   do C

heigth = int(input("What's your heigth: ?"))
bill = 0

if heigth >= 120:
    print("You can ride")
    age = int(input("What's your age: "))
    if age <= 18:
        bill = 7 
        print("$7")
    elif age <= 12:
        bill = 5
        print("$5")
    elif 45 <= age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("$12")
        
    wants_photo = input("Do you want to have a photo tak? type ""y"" for Yes and ""n"" for No.")
    if wants_photo == "y":
        bill += 3
        
        print(f"Your finall bill is {bill}")
else:
    print("You can't ride")
    
