age=int(input("Enter age: "))

if age <= 2:
    print("The person is baby")
elif age <= 4:
    print("Toddler")
elif age <= 13:
    print("The person is a kid")
elif age <= 20:
    print("The person is a teenager")
elif age <= 65:
    print("The person is adult")
else:
    print("The person is an elder")   