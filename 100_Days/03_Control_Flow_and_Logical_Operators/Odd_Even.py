x = int(input("Give me a number: "))

def main():
    if odd_even(x):
        print ("Even")
    else: 
        print("Odd")
    

def odd_even(n):
    return n % 2 == 0 


main()