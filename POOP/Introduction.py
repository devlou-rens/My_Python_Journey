class Intro:
    def __init__(self, full_name, age): #constructor
        self.full_name = full_name #instance variable
        self.age = age #instance variable
    
    def introduce(self): #method
        print(f"Hi I'm {self.full_name}, and I'm {self.age} years old.")

introObj = Intro("devlou-rens", 21) #object

#display
print(introObj.full_name) #Output: devlou-rens
print(introObj.age)       #Output: 21
introObj.introduce()      #Output: Hi I'm devlou-rens, and I'm 21 years old.