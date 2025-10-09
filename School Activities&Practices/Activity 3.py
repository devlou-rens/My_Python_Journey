# Define the factorial function
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1  # Factorial of 0 is 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Prompt the user to input a number
num = int(input("Enter a number: "))

# Calculate and display the factorial
print(f"The factorial of {num} is {factorial(num)}")