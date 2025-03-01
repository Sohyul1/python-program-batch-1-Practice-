# Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.
# Ask for user input
while True:
    num1 = float(input("Enter a number: "))
    num2  = float(input("Enter another number: "))

# Get the product
    product = num1 * num2
# Print the product
    print(f"The product of the given numbers is {product}")

    restart = input("\nWanna try again?(yes/no):").lower()
    # Loop
    if restart == "no":
        print("Good bye!")
        break
