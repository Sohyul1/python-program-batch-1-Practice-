# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
# Ask for user input
while True:
    num1 = float(input("Enter the base number: "))
    num2  = float(input("Enter the exponent: "))
    
# Get the sqaured of the numbers
    expo = num1 ** num2
    # Print the output 
    print(f"The squared value of the given numbers is {expo}.")

    restart = input("\nWanna try again?(yes/no):").lower()
    # Loop
    if restart == "no":
        print("Good bye!")
        break
