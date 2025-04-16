
#Polymorphism is the ability of different classes to use the same method 
# name but implement it in different ways.

#Parent class
class Muffins: 
    def __init__(self, name, flavour):
        self.name = name
        self.flavour = flavour

    def describe(self):
        print(f"This is a {self.name} muffin with extra {self.flavour} flavour")      

#Children classes
class Vanilla(Muffins): 
    def describe(self):
        print(f"This is a {self.name} muffin with {self.flavour}.")      

class Carrot(Muffins): 
    def describe(self):
        print(f"This is a {self.name} muffin with {self.flavour}.") 

#Creating objects for the classes
vanilla_muffin = Vanilla("Vanilla", "Blueberries")
carrot_muffin = Carrot("Carrot", "Nuts")

#calling each objects describe method to showcase polymorphism
vanilla_muffin.describe()
carrot_muffin.describe()

