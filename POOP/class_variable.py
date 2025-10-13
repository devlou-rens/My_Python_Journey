''' 
A class variable is a variable that is shared by all objects (instances) of a class.
It belongs to the class itself, not to any one object.
'''

class Student:

    class_var = 2025 #class variable (shared by all student)
    student_num = 0

    def __init__(self, name, age): #constructor
        self.name = name           #instance variable
        self.age = age             #instance variable
        Student.student_num += 1   #calculate how many students


#Create a Objects
student1 = Student("Naruto", 24)
student2 = Student("Hinata", 23)
student3 = Student("Sakura", 23)
#dispaly student1
print(student1.name)
print(student1.age)
print(f"Year: {student1.class_var}") #with class variable

print()

#display student2
print(student2.name)
print(student2.age)
print(f"Year: {student2.class_var}") #with class variable

print()

#display student3
print(student3.name)
print(student3.age)
print(f"Year: {student3.class_var}") #with class variable

print()
print(f"Total Student: {Student.student_num}") #with class variable of student_num that calculate how many students