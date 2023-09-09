'''
        Program Name: M03 Lab Case Study
                   Author Name: David Tellez
Last Date Modified: 09/08/2023

This program accepts user input for a car. The app will store "car" into the vehicle type in your Vehicle super class. 
The app will then ask the user for the year, make, model, doors, and type of roof and store the data in the attributes above.
The app will then output the data in an easy-to-read and understandable format
'''
class Vehicle:
 type1 = "car"
 type2 = "truck"
 type3 = "plane"
 type4 = "boat"
 type5 = "broomstick"

class Automobile(Vehicle):
   def __init__(self, year, make, model, door, roof):
      self.year = year 
      self.make = make
      self.model = model
      self.door = door
      self.roof = roof

my_car = Automobile(2023, "Honda", "Civic", 4, "sunroof")

my_car.type1 = "car"

my_car.year = input("What year is the car?: ")
my_car.make = input("What make is the car?: ")
my_car.model = input("What model is the car?: ")
my_car.doors = input("Is the car 4 door or 2 doors?: ")
my_car.roof = input("What type of roof does the car have?: ")

print("Vehicle Type: ",my_car.type1)
print ("Year: ",my_car.year)
print ("Make: ",my_car.make)
print ("Model: ",my_car.model)
print ("Number of doors: ",my_car.doors)
print ("Type of roof: ",my_car.roof)