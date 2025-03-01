# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
# Ask the user to input a number
num1 = float(input("Enter a number: "))
num2  = float(input("Enter another number: "))

# Determine the biiger number
# Print the bigger number if there is 
if num1 > num2:
    print(f"{num1} is the biger number")
elif num2 > num1:
    print(f"{num2} is the bigger number")
else:
    print("The numbers you entered are equals")


