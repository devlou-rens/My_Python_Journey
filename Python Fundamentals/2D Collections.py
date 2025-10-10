#fruits =     ["mansanas", "ubas", "mangga", "lubi"]
#vegetables = ["petchay", "talong", "repolyo", "balatong"]
#meats =      ["isda", "baka", "manok", "baboy"]


#groceries = [fruits, vegetables, meats]

#print(groceries[2][1])

#groceries = [["mansanas", "ubas", "mangga", "lubi"],
  #           ["petchay", "talong", "repolyo", "balatong"],
   #          ["isda", "baka", "manok", "baboy"]]

#for colections in groceries:
#    print(colections)

#using nested loop

#for collection in groceries:
 #   for food in collection:
   #     print(food, end=" ")
    #print()


# practice phone button number
num_pad = ((1, 2 ,3),
           (4, 5 ,6),
           (7, 8 ,9),
           ("*", 0 ,"#"))

for num in num_pad:
    for numbers in num:
        print(numbers, end=" ")
    print()