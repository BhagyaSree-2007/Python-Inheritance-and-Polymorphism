'''Write Python code to implement the Vehicle, Car, and Bike class
hierarchy for different types of vehicles. The base class is Vehicle,
which has attributes ‘make’ and ‘year’, and a method that prints the
‘make’ and ‘year’ of the vehicle.'''
class Vehicle:
    def Getdetails(self):
        self.make = input("Enter Brand: ")
        self.year = int(input("Enter Year: "))
        self.colour = input("Enter Colour: ")

    def display_info(self):
        print("\nBrand:",self.make,"\nYear:",self.year,"\nColour:",self.colour)
       
class Car(Vehicle):
    def GetCarDetails(self):
        self.Getdetails()
        self.model = input("Enter Model: ")
        self.capacity = input("Enter Capacity: ")

    def Display_car(self):
        self.display_info()
        print("\nModel:",self.model,"\nCapacity:",self.capacity)

class Bike(Vehicle):
    def GetbikeDetails(self):
        self.Getdetails()
        self.type = input("Enter Type: ")
        self.mileage = input("Enter Mileage: ")

    def Display_bike(self):
        self.display_info()
        print("Type:",self.type,"\nMileage:",self.mileage)

print("--- Car Entry ---")
my_car = Car()
my_car.GetCarDetails()
my_car.Display_car()
print("\n--- Bike Entry ---")
my_bike = Bike()
my_bike.GetbikeDetails()
my_bike.Display_bike()
