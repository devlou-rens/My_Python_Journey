#Basic_Calculator
print("_____________________Enjoy Computing_____________________")
try:
    num1=float(input("Enter first number: "))
    operation=input("(Please choose Operator)\n"
                    "For Addition[+]\n"
                    "For Subtraction[-]\n"
                    "For Multiplication[*]\n"
                    "For Division[/]\n"
                    "Enter the operation: ")
    num2=float(input("Enter second number: "))


    while True:
        if operation == '+':
            print("The sum is ", num1 + num2)
        elif operation == '-':
            print("The difference is: ", num1 - num2)
        elif operation == '*':
            print("The product is: ", num1 * num2)
        elif operation == '/':
            if num2 == 0:
                print("Division by zero is not allowed.")
            else:
                print("The quotient is: ", num1 / num2)
        else:
            print("Invalid Input")

        print()
        num1 = float(input("Enter first number: "))
        operation = input("(Please choose Operator)\n"
                          "For Addition[+]\n"
                          "For Subtraction[-]\n"
                          "For Multiplication[*]\n"
                          "For Division[/]\n"
                          "Enter the operation: ")
        num2 = float(input("Enter second number: "))



except:
    print("Syntax Error!")



    
