#lists = [] ordered and changeable. Duplicates OK
#sets = {} unordered and immutable, but Add/Remove OK. NO duplicates
#tuple = () ordered and unchangeable. Duplicates OK. FASTER
sections = ["A", "B", "C", "D"]
#print(dir(sections))
#print(help(sections))
#print(len(sections))
#print('L' in sections)
#print(section[0])
#sections[0] = "L" # change list
#sections.append("L") # add list
#sections.remove("C") # remove list
#sections.insert(0, "L") # adding list but no remove
#sections.sort()
#sections.reverse()
#sections.clear() # remove all list
#print(sections.index("A")) # showing index in list
#print(sections.count("A")) # count list
sections.copy()
print(sections)

#for section in sections:
#    print(section)