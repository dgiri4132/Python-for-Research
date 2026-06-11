#OOP Object-oriented programming
# you create objects and class and manipulate them

""" When you create individual objects from the class, each object is automatically equipped with
    the general behavior; you can then give each object whatever unique trats you desire
    
    Starting with basics: """
class Dog():
    """ A simple attemp to model a dog."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        print(self.name.title() + " rolled over!")

""" A fuction that's part of a class is a method. The only practical difference is the way we call methods.
the __init__() method is a special method Python runs automatically whenever we create a new instance based on the Dog class
The function has self which passes automatically always and other parameters set up to be general.
Any variable with self as prefix is accessible to every instace created from the class
Here in the dog example we don't need special arguments with the methods roll_over and sit and also that name is accesile 
entirely, so nothing is needed except for self.
You can also make an instance from a class."""
my_dog=Dog('willie', 6)


print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is "+str(my_dog.age) + " years old.")

# Can also create multiple instances
your_dog=Dog('lucy', 3)

# Calling methods
my_dog.sit()
my_dog.roll_over()

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is "+str(your_dog.age) + " years old.")

your_dog.roll_over()
your_dog.sit()


# Setting a Default Value for an Attribute

class Car():
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        print(self.make.title()+ " " + self.model.title() + " " + str(self.year))
    
    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading) + " miles on it.")
    
my_new_car=Car('audi', 'a4', 2016)
my_new_car.get_descriptive_name()
my_new_car.read_odometer()
my_new_car.odometer_reading=2300
my_new_car.read_odometer()