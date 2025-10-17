"""
Defined using the abc (Abstract Base Class) module.
Contains abstract methods, which are methods declared but not implemented in the base class.
Any subclass that inherits from an abstract class must implement all its abstract methods.
You cannot create an object of an abstract class.
"""

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Motorcycle(Vehicle):

    def go(self):
        return "You drive the motorcycle!" #using return is more flexible and reusable
    
    def stop(self):
        print("You stop the motorcycle!") # Use print only for showing or testing results.

play = Motorcycle()

print(play.go())
play.stop()