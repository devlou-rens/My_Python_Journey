print("--------------Simple Bank--------------")
print()


user_name = ''
current_balance = 0
deposit = 0
withdraw = 0
total_balance = 0

while True:
    user_name = input("Enter your username: ")
    if user_name == '':
        print("Please enter your username!")
    elif not user_name.isalpha():
        print("Your username can't contain numbers or space")
    else:
        break
while True:
    credit_number = input("Enter your last 4 digit of your credit number: ")
    if credit_number == '':
        print("You can't proceed! Please enter again!")
    elif not credit_number.isdigit():
        print("Invalid! Can't contain letters")
    elif len(credit_number) > 4:
        print("Your credit number can't be more than 4 digits")
    elif len(credit_number) < 4:
        print("Your credit number can't be less than 4 digits")

    else:
        break
print()
print("-----------------------------------------------------")
print(f"Username: {user_name}")
result = credit_number[-4:]
print(f"Credit Number: XXXX-XXXX-XXXX-{result}")
print("-----------------------------------------------------")
print()

while True:
    current_balance = float(input("Enter your current balance: "))
    if current_balance < 0:
        print("Need to enter your current balance!: ")
    else:
        break
print()
print("-----------------------------------------------------")
print(f"Username: {user_name}")
print(f"Balance: ${current_balance:,.2f}")
print("-----------------------------------------------------")
print()


while True:
    qa = input("You want to Deposit or Withdraw? D/W if no select N: ").upper()
    if qa == 'N':
        print(f"Thank you {user_name}, come again!")
        break
    elif qa == 'D':
        while True:
            deposit = float(input("Amount of deposit: "))
            if deposit < 0:
                print("Please enter again!: ")
            else:
                break
        print()
        total_balance = current_balance + deposit
        print("-------------------------------------------------------------------")
        print("Deposit successfully!")
        print("-------------------------------------------------------------------")
        print(f"Current Balance: ${current_balance:,.2f}")
        print("-------------------------------------------------------------------")
        print(f"Deposit: ${deposit:+,.2f}")
        print("-------------------------------------------------------------------")
        print(f"Your total balance is ${total_balance:,.2f}")
        print("-------------------------------------------------------------------")
        print()
    elif qa == 'W':
        while True:
            withdraw = float(input(f"Balance(${total_balance:,.2f}) Amount of Withdraw: "))
            if withdraw <= 0:
                print("You can't withdraw less than or equal to zero!")
                break
            else:
                break
        print()
        total_balance -= withdraw
        print("---------------------------------------------------------------------")
        print("Withdraw successfully!")
        print("---------------------------------------------------------------------")
        print(f"Current Balance: ${current_balance:,.2f}")
        print("---------------------------------------------------------------------")
        print(f"Withdraw: $-{withdraw:,.2f}")
        print("---------------------------------------------------------------------")
        print(f"Your total balance is ${total_balance:,.2f}")
        print("---------------------------------------------------------------------")
        print()


