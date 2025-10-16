#| Concept                    |         Meaning          |      Example / Use           |
#| -------------------------- | ------------------------ | ---------------------------- |
#| **Multilevel Inheritance** | Chain of inheritance     | `Grandfather → Father → Son` |
#| **Multiple Inheritance**   | Inherit from 2+ parents  | `Son(Father, Mother)`        |
#| **`super()`**              | Calls next parent in MRO | `super().__init__()`         |
#| **`__init__()`**           | Constructor method       | Initializes object data      |
#| **`**kwargs`**             | Keyword arguments        | Makes `super()` flexible     |

#lolo class
class Grandfather:
    def __init__(self, grand_Father, **kwargs):
        super().__init__(**kwargs)
        self.grand_Father = grand_Father

    def intro_Grandfather(self):
        print(f"Grandfather's name: {self.grand_Father}")

# papa inherits lolo (multilevel)
class Father(Grandfather):
    def __init__(self, father, **kwargs):
        super().__init__(**kwargs)  # pantawag kay lolo
        self.father = father
    
    def intro_Father(self):
        print(f"Father's name: {self.father}")

# mama parent class
class Mother:
    def __init__(self, mother, **kwargs):
        super().__init__(**kwargs) # para matawagan si mama sin intiro
        self.mother = mother

    def intro_Mother(self):    
        print(f"Mother's name: {self.mother}")

# bata inherit (multiple + multilevel)
class Son(Father, Mother):
    def __init__(self, grand_Father, father, mother, son):
        super().__init__(grand_Father = grand_Father, father = father, mother = mother) #dahil sa **kwargs and super() natawagan intiro sin bata
        self.son = son

    def intro_Son(self):
        print(f"Son's name: {self.son}")
    
    def Introduction(self):
        print(f"Hi ako si {self.son}, si {self.grand_Father} ay mahilig sa chix hehe, \nang {self.father} ko naman ay isang mikaniko, \nsi {self.mother} ko naman ay isang chismosa hehe joke lang")

# Create object
Intro = Son("Lolo Jose","Papa Juan","Mama Alice", "Nonoy")
Intro.intro_Grandfather()
Intro.intro_Father()
Intro.intro_Mother()
Intro.intro_Son()
print()
Intro.Introduction()