# Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
# Make an empty list
empty = []
# Filter out the even numberss
for nums in range(0, 101):
    if nums % 2 == 0:
        empty.append(nums)
    
# Print the even numbers
print(f"\nThe even numbers are:\n\n{empty}")



