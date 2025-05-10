# Activity 2: Polymorphism with move() Method
class Vehicle:
    def move(self):
        print("The vehicle moves")

# Subclasses with different move() implementations
class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("Sailing on water")

# Function to demonstrate polymorphism
def show_movement(vehicle):
    vehicle.move()

# Create objects
car = Car()
plane = Plane()
boat = Boat()

# Test polymorphism
show_movement(car)
show_movement(plane)
show_movement(boat)
