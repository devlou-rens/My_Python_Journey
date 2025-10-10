# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicate

animals = {"Aso": "Dog",
           "Pusa": "Cat",
           "Ibon": "Bird",
           "Unggoy": "Monkey"}

# print(dir(animals))
# print(help(animals))

#print(animals.get("Aso"))

#if animals.get("Snake"):
#    print("This Animal exists")
#else:
#    print("This Animal doesn't exists")

animals.update({"Ahas": "Snake"})
animals.update({"Ibon": "Aso"})
print(animals)