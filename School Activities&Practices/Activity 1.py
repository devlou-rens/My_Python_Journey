# Prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the absolute value of both numbers
print(f"The absolute value of {num1} is {abs(num1)}")
print(f"The absolute value of {num2} is {abs(num2)}")

# Calculate and display the power of num1 raised to num2
print(f"{num1} raised to the power of {num2} is {pow(num1, num2)}")

# Round num1 to 2 decimal places
print(f"{num1} rounded to 2 decimal places is {round(num1, 2)}")

# Find and display the maximum of the two numbers
print(f"The maximum of {num1} and {num2} is {max(num1, num2)}")