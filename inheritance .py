class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        return f"Brand: {self.brand}, Speed: {self.speed} km/h"

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def display_info(self):
        return super().display_info() + f", Doors: {self.doors}"

class Bike(Vehicle):
    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type

    def display_info(self):
        return super().display_info() + f", Type: {self.type}"

car = Car("Toyota", 180, 4)
bike = Bike("Yamaha", 120, "Sport")
print(car.display_info())
print(bike.display_info())