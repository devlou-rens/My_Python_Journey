''' 
A class variable is a variable that is shared by all objects (instances) of a class.
It belongs to the class itself, not to any one object.
'''

class Student:

    class_var = 2025 #class variable (shared by all student)

    def __init__(self, name, age): #constructor
        self.name = name           #instance variable
        self.age = age             #instance variable

#Create a Objects
student1 = Student("Naruto", 24)
student2 = Student("Hinata", 23)

#dispaly student1
print(student1.name)
print(student1.age)
print("Year:", student1.class_var) #with class variable

print()

#display student2
print(student2.name)
print(student2.age)
print("Year:", student2.class_var) #with class variable