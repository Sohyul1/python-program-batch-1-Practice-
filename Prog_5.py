# Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
# Ask for user input
while True:
    num1 = float(input("Enter your dividend: "))
    num2  = float(input("Enter the divisor: "))

# Get the quotient
    quotient = num1 / num2
# Print the quotient
    print(f"The quotient of the given numbers is {quotient}.")

    restart = input("\nWanna try again?(yes/no):").lower()
    # Loop
    if restart == "no":
        print("Good bye!")
        break