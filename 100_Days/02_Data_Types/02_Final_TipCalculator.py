### Project: 100 Days of Code - The Complete Python Pro Bootcamp for 2024
# 02_Data_Types/02_Final_TipCalculator.py
#1. Create a greeting for your program.
#2. Ask the user for the total bill.
#3. Ask the user for the tip percentage they would like to give.
#4. Ask the user for the number of people to split the bill between.
#5. Calculate the total tip amount and the total bill amount including the tip.
#6. Calculate the amount each person should pay.
#7. Round the amount each person should pay to 2 decimal places.
#8. Print the amount each person should pay.


#1. Create a greeting for your program.
print("Welcome to the tip calculator!")

#2 Ask the user for the total bill. 
bill = float(input("What was the total bill? $"))

#3 Ask the user for the tip percentage they would like to give.
tip = int(input("What percentage tip would you like to give?, please enter a number: 10, 12, or 15?: "))

#4 Ask the user for the number of people to split the bill between.
people = int(input("How many people to split the bill?"))

#5 Calculate the total tip amount and the total bill amount including the tip.
total_tip = bill*(tip/100)
tottal_bill = bill + total_tip

#6 Calculate the amount each person should pay.
amaount_per_person = tottal_bill/people

#7 Round the amount each person should pay to 2 decimal places.
final_amount = round(amaount_per_person, 2) #final amount should be rounded to 2 decimal places.

#8 Print the amount each person should pay.
print(f"The total bill is: ${tottal_bill:.2f}")
print(f"Each person should pay: ${final_amount:.2f}")