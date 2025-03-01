# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

# Ask the user to input a number
while True:
    num1 = float(input("Enter a number: "))
    num2  = float(input("Enter another number: "))

    # Determine the bigger number
    # Print the bigger number if there is else ask for another input
    if num1 > num2:
        print(f"{num1} is the bigger number.")
    elif num2 > num1:
        print(f"{num2} is the bigger number.")
    else:
        print("Please enter two different numbers.")

    ans = input("\n(Type restart/exit): ").lower().strip()
    if ans != "restart":
        print("Good bye!")
        break
        
       
 


