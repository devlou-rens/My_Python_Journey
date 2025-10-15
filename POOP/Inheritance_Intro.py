"""
Inheritance allows a class (called the child or subclass) to use or extend the properties and 
methods of another class (called the parent or superclass).
"""
# Parent Class
class Father:
    def __init__(self, father_name): #constructor
        self.father_name = father_name      #instance Variable

    def introduce_Father(self): #Method for father
        print(f"Father's name: {self.father_name}")

#Second Parent Class
class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

    def introduce_Mother(self): #Method for mother
        print(f"Mother's name: {self.mother_name}")

# Child Class (inherits from both Father and Mother)
class Child(Father, Mother):
    def __init__(self, father_name, mother_name, child_name): #incude the parameter in the parent class in child class
        Father.__init__(self, father_name)   # manually call Father constructor
        Mother.__init__(self, mother_name)   # manually call Mother constructor 
        self.child_name = child_name #instance Variable

    def introduce_Child(self): #method
        print(f"Child's name: {self.child_name}")

    def introduce(self):# overrides parent's method for itroduce
        print(f"I am {self.child_name}, child of {self.father_name} and {self.mother_name}.")


# Create Object
Intro = Child("Arisu", "Usagi", "Lourens")

# Method Calls
Intro.introduce_Father()
Intro.introduce_Mother()
Intro.introduce_Child()
Intro.introduce()