chickens= 0
cows= 0
pigs= 0
total_legs= 0
chickenleg= 2
cowsleg= 4
pigsleg= 4
chickens=int(input("Input number: "))
cows=int(input("Input number: "))
pigs=int(input("Input number: "))


total_legs = (chickens * chickenleg) + (cows * cowsleg) + (pigs * pigsleg)

print("Total number of legs: ", total_legs)