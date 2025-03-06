# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
# Make an empty list
# Ask for user input
numbers = []
while True:
    numbers.clear() 
    for nums in range(1, 11):
        num = float(input(f"Enter number {nums}: "))
        # Filter out the odd numbers
        if num % 2 != 0:
            numbers.append(num)
    
    total = len(numbers)
    # Print the odd numbers
    print(f"There is a total of {total} odd numbers.")
    
    # Loop
    ans = input("Wanna go again?(yes/no): ")
    if ans == "no":
        print("Good Bye!")
        break

    




  

