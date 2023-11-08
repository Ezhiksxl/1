#1
class Shape:
    def __init__(self, color):
        self.color = color
        self.area = 0

    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        self.area = 3.14 * (self.radius ** 2)

circle1 = Circle("красный", 5)
circle2 = Circle("синий", 7)

circle1.calculate_area()
circle2.calculate_area()

print("Круг 1:")
print("Цвет:", circle1.color)
print("Радиус:", circle1.radius)
print("Площадь:", circle1.area)

print("Круг 2:")
print("Цвет:", circle2.color)
print("Радиус:", circle2.radius)
print("Площадь:", circle2.area)

#2
class Animal:
    def voice(self):
        pass
        
class Dog(Animal):
    def voice(self):
        super().voice()
        print("woof")
        
class Cat(Animal):
    def voice(self):
        super().voice()
        print("myaaaauuuuu")

dog=Dog()
cat=Cat()
dog.voice()
cat.voice()

#3
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Год выпуска: {self.year}")

class SportsCar(Car):
    def __init__(self, brand, year, max_speed):
        super().__init__(brand, year)
        self.max_speed = max_speed

    def display_info(self):
        super().display_info()
        print(f"Максимальная скорость: {self.max_speed}")

car1 = SportsCar("Ferrari", 2020, 350)
car1.display_info()
print()

car2 = SportsCar("Porsche", 2019, 320)
car2.display_info()

#5
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print(f"The {self.brand} vehicle is starting.")

    def stop(self):
        print(f"The {self.brand} vehicle has stopped.")


class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery_capacity):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.battery_charge = 0

    def start(self):
        super().start()
        self.display_battery_status()

    def charge(self, amount):
        self.battery_charge += amount
        if self.battery_charge > self.battery_capacity:
            self.battery_charge = self.battery_capacity

    def display_battery_status(self):
        print(f"The battery charge of the {self.brand} electric car is {self.battery_charge}/{self.battery_capacity}.")
        
car = ElectricCar("Tesla", 200, 100)
car.start()
car.charge(50)
car.start()

#6
class Building:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def display_info(self):
        print(f"Building name: {self.name}")
        print(f"Building area: {self.area} square meters")


class OfficeBuilding(Building):
    def __init__(self, name, area, num_workplaces):
        super().__init__(name, area)
        self.num_workplaces = num_workplaces

    def display_info(self):
        super().display_info()
        print(f"Number of workplaces: {self.num_workplaces}")

building1 = Building("Residential House", 200)
building1.display_info()

office_building1 = OfficeBuilding("Office Tower", 1000, 200)
office_building1.display_info()