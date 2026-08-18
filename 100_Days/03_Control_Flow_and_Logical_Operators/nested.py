#Nested condition elif

#if condition:
#   if another condition:
#       do this:
#    elif: 
#       do this:
#else:
#       do this

higth = int((input("Tell me your higth: ")))

if higth >= 120:
    print("You Can ride")
    age = int(input("What' is your age?: "))
    if age <= 18:
        print("Please pay $7")
    else:
        print("Plase pay $12")
else: 
    print("You can't ride")
    


