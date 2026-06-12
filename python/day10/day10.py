# We start today with importing classes
from day09fr import Car
my_new_car=Car('audi','a4', 2016)
my_new_car.get_descriptive_name()
my_new_car.odometer_reading=23
my_new_car.read_odometer()

#Importing multiple classes is the same as well
# from car import Car, ElectricCar

#You can also import the whole module and then access the classes you need

import day09fr

my_bettle=day09fr.Car('volkswagen','beetle',2016)
my_tesla=day09fr.ElectricCar('tesla','roadster',2016)

# Importing all classes from a module

from day09fr import *

#Importing from the python standard library

from collections import OrderedDict

favorite_languages=OrderedDict()
favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'

for name, language in favorite_languages.items():
    print(name.title() + " 's favorite language is " + language.title() + ".")
