print(r"""
.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
.            _.,.__       .                                   .
.           ((o\\o\))     .                                   .
.     .-.    `  \\``      .    A tropical island              .
.  __(   )___.o"^^".,___  .                                   .
.     ===    ~~~~~~~~     .                                   .
.      ==             ldb .                                   .
.       =                 .                                   .
.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
""")

print("Welcome to Treasure Island.\nYour mission is to find the treasure")

choice_one = input("left or right?: ").strip().lower()

if choice_one == "left":
    choice_two  = input("swim or wait: ")
   
    if choice_two == "wait":
        door = input("Which door?, red / blue / yellow: ")
        
        if door == "red":
            print("Burned by fire.\nGame Over")
        elif door == "yellow":  
            print("You Win!")
        else: 
            print("Attacked by trout.\nGame Over")
   
    else:
       print("Attacked by trout.\nGame Over")
    
else: 
    print("Fall into a hole.\nGame Over.")