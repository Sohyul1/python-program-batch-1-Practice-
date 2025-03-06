# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
# Make an empty list
numbers = []
# Ask for user input
while True:
    numbers.clear()  
    for nums in range(1, 11):
        num = float(input(f"Enter number {nums}: "))
        numbers.append(num)
# Get the sum 
    total = sum(numbers)
    # Print The sum
    print(f"The sum of the given numbers is {total}.")
# Loop 
    ans = input("Wanna add again?(yes/no): ")
    if ans == "no":
        print("Good Bye!")
        break