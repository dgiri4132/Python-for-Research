#Reviewing yesterday a little bit.
# Setting a Default Value for an Attribute

class Car():
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        print(str(self.year)+' ' +self.make + " "+ self.model )

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        if mileage>= self.odometer_reading:    
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading+=miles
        
"""

#Inheritance
 If you are writing a class which is a specialized version of another class you wrote, you can use 
    inheritance. It takes on all attributes of the first class hence forming parent and child class.



#Continued from my_tesla.describe_battery()

 As you start writing codes, you'll have more and more classes and stuff like that i.e.
it will become more complex, that is why we can call instances as attributes
see from the example below"""

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size=battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")



# The init method for a child class

class ElectricCar(Car):
    def __init__(self, make, model, year):
        # The super function is a special function which helps make the connection between the parent and child class
# Defining attributes and methods for the child class
        super().__init__(make, model, year)
        self.battery=Battery()

    # Overriding Methods from the parent class
    # To override the methods from parent class, you have can define the same function and write something 
