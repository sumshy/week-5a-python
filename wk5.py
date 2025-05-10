# Activity 1 Superhero Class with Inheritance & Encapsulation
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self._power = power           
        self.city = city

    def introduce(self):
        print(f"Hi, I'm {self.name}, and I protect {self.city}!")

    def use_power(self):
        print(f"{self.name} uses {self._power} to save the day!")

# Inherited class
class TechHero(Superhero):
    def __init__(self, name, power, city, gadget):
        super().__init__(name, power, city)
        self.gadget = gadget

    def use_gadget(self):
        print(f"{self.name} activates their {self.gadget}!")

# Creating an object
hero1 = TechHero("CircuitMan", "Electric Surge", "Metro City", "Tesla Blade")
hero1.introduce()
hero1.use_power()
hero1.use_gadget()
