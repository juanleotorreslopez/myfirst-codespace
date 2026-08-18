### Project: 100 Days of Code - The Complete Python Pro Bootcamp for 2024
# 01_Variables/01_Final_BandGenerationName.py
#1. Create a greeting for your program.
#2. Ask the user for the cty that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://www.w3schools.com/python/ref_func_input.asp


def main():
    print("Welcome to the Band Name Generator.")
    city = input("What's the name of the city that you grew up in?:\n")
    pet = input("What's the name of a pet?:\n")
    print("Your band name could be " + city + " " + pet)

if __name__ == "__main__":
    main()
    
    
    