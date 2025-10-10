# Function
first_name = input("First Name: ")
last_name = input("Last Name: ")

def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + " " + last_name
full_name = create_name(first_name, last_name)
print(f"Welcome {full_name}")


#example
num1 = float(input("First number: "))
num2 = float(input("Second number: "))

def addition(num1, num2):
    add = num1 + num2
    return add
print(f"Result: ", addition(num1, num2))