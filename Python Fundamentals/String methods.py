#name = input("Enter your name: ")
#phone_number = input("Enter your phone number: ")
#name = len(name)
#name = name.find("o")
#name = name.rfind("o")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result= name.isdigit()
#result= name.isalpha()
#result = phone_number.count("-")
#phone_number = phone_number.replace("-", " ")
#print(phone_number)

user_name = input("Enter your username: ")
user_name.isdigit()
if len(user_name) > 12:
    print("Your username can't be more than 12 characters")
elif not user_name.find(" ") == -1:
    print("Your username can't contain spaces")
elif not user_name.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {user_name}!")