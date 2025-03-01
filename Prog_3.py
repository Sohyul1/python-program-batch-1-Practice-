# Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.
# Ask for user input
while True:
    num1 = float(input("Enter a number: "))
    num2  = float(input("Enter another number: "))

# Get the sum
    sum = num1 + num2
# Print the sum
    print(f"The sum of the given numbers is {sum}")
    
    restart = input("\nWanna try again?(yes/no):").lower()
    # Loop
    if restart == "no":
        break

