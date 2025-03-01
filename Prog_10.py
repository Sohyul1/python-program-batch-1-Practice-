# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
# Make an empty list
empty = []

# Filter out the numbers ending with 0 
for nums in range (0,101):
    if nums % 10 != 0:
        empty.append(nums)
# Print the rest of the  numbers
print(f"\nThe numbers are:\n\n{empty}")