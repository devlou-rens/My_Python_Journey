num=int(input("Enter number: "))

for i in range(11):
    print(i, "x" , num , "=", num*i)

print()

for i in range(1,6):
    print("*" * i)

print()

for i in reversed(range( 1,6)):
    print("*" * i)

print()

num=int(input("Enter Number: "))
        
while num != 10:
    if num < 10:
        print("Higher")
    elif num > 10:
        print ("Lower")
    num=int(input("Enter Number: "))
print("The number was", num)

print()

name=input("Enter your name: ")
print("Hello", name)

print()

num1=int(input("Enter First number: "))
num2=int(input("Enter Second number: "))
operator=input("Choose Operator \n [A] for Addition(+) \n [B] fot Subtraction(-) \n [C] for Multiplication(*) \n [D] for Division(/) \n Enter Operator: ")

A='+'
B='-'
C='*'
D='/'
while True:
    if operator == 'A':
        print("The result is ", num1 + num2)
    elif operator == 'B':
        print("Tne result is ", num1 - num2)
    elif operator == 'C':
        print("The result is ", num1 * num2)
    elif operator == 'D':
        print("The result is ", num1 / num2)
    num1=int(input("Enter First number: "))
    num2=int(input("Enter Second number: "))
    operator=input("Choose Operator \n [A] for Addition(+) \n [B] fot Subtraction(-) \n [C] for Multiplication(*) \n [D] for Division(/) \n Enter Operator: ")
print("Syntax Error")


