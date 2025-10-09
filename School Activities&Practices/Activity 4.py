# Initialize an empty list
numbers = []

# Add 5 numbers to the list using append()
for _ in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)

# Remove the first occurrence of a number using remove()
num_to_remove = float(input("Enter a number to remove from the list: "))
if num_to_remove in numbers:
    numbers.remove(num_to_remove)
else:
    print(f"{num_to_remove} not found in the list.")

# Sort the list in ascending order using sort()
numbers.sort()

# Calculate and print the sum of all numbers in the list
total_sum = sum(numbers)
print(f"Sorted list: {numbers}")
print(f"Sum of the numbers in the list: {total_sum}")