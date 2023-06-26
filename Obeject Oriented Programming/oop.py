"""Classes and Objects:
A class is a blueprint for creating objects, while an object is an instance of a class. Classes define the attributes (data) and methods (functions) 
that objects of that class will have. Here's an example:"""
class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f"The {self.color} {self.brand} car's engine is starting")
"""Creating Objects:
To create an object from a class, you need to instantiate it using the class name followed by parentheses. Here's an example:"""
my_car = Car("Tesla", "red")

"""Accessing Attributes and Methods:
You can access an object's attributes and methods using the dot notation (.). Here's an example:"""
print(my_car.brand)
print(my_car.color)
my_car.start_engine()

#Example 2 --F1
class formula1:
    def __init__(self,driver,racing_team,power_trains,points):
        self.driver = driver
        self.racing_team = racing_team
        self.power_trains = power_trains
        self.points = points
    
    def race_results(self):
        print(f"The monaco winner is {self.driver} of {self.racing_team},powered by {self.power_trains} with {self.points} points")

f1_results = formula1("Max verstappen", "Redbull racing","Rebdull power Trains","25")
print(f1_results.driver)
print(f1_results.racing_team)
print(f1_results.power_trains)
print(f1_results.points)

f1_results.race_results()


"""Inheritance
Inheritance is a mechanism where one class (child/subclass) derives properties from another class (parent/superclass). 
It allows you to create a hierarchy of classes with shared attributes and methods. Here's an example:"""
class ElectricCar(Car):
    def charge_battery(self):
        print(f"The {self.color} {self.brand} electric car is charging its battery")

my_electric_car =ElectricCar("Kia", "blue")
my_electric_car.start_engine()
my_electric_car.charge_battery()



#Example 2 --f1 
class formulaE(formula1):
        def fE_results(self):
            print(f"The winning formualaE driver is {self.driver} for the {self.racing_team} with {self.points} points")

fomulaelectric = formulaE("Lawson Davis","Mercedes","HPPT", "45")
fomulaelectric.fE_results()           



"""Polymorphism:
Polymorphism allows objects of different classes to be treated as objects of a 
common superclass. It enables different objects to respond to the same method in different ways. 
Here's an example:"""
def describe_vehicles(vehicle):
    print(f"The {vehicle.color} {vehicle.brand} is a vehicle")

my_vehicle = Car("BMW","Black")
my_electric_vehicle =ElectricCar("nISSAN", "Green")

describe_vehicle(my_vehicle)
describe_vehicle(my_electric_vehicle)