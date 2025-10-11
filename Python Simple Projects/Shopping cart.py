foods = []
prices = []
totals = 0

while True:
    food = input("Enter a foods or drinks to buy. (q for quit): ").capitalize()
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter a price of {food}: $"))
        foods.append(food)
        prices.append(price)
print("---------Shopping Cart---------")

for food in foods:
    print(food, end=" ")

for price in prices:
    totals += price
print()
print(f"Your total is: {totals}")


