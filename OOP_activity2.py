#Base class
class Animals:
    def __init__(self, food):
        self.food = food

    def eat(self):
        print(f"This animal eats {self.food}.")

#Children classes
class Chicken(Animals):
    def eat(self):
        print(f"The chicken eats {self.food}.")

class Horse(Animals):
    def eat(self):
        print(f"The horse eats {self.food}.")

#Creating objects for the classes
chicken = Chicken("corn")
horse = Horse("hay")

#calling each objects eat method to showcase polymorphism
chicken.eat()
horse.eat()