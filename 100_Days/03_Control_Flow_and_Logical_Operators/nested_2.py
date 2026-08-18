#elif more conditionals 
# if condition1:
#    do A
# elif condition 2:
#    do B
# else: 
#   do C

heigth = int(input("What's your heigth: ?"))


if heigth >= 120:
    print("You can ride")
    age = int(input("What's your age: "))
    if age <= 18:
        print("$7")
    elif age <= 12:
        print("$5")
    else:
        print("$12")
else:
    print("You can't ride")