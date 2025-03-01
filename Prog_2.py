# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

# Ask the user to input a number
while True:
    num1 = float(input("Enter a number: "))
    num2  = float(input("Enter another number: "))

# Determine the numbers are equal
# Print the output
    if num1 == num2:
        print("Equal")
    else:
        print("Not equal")

    ans = input("Try again?(yes/no): ").lower()
    if ans == "no":
        print("Good bye!")
        break

