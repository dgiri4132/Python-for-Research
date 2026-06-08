#Passing a Arbitrary Number of Arguments
# To pass a random number of arguments, use asterik before the definition parameter
#Single asterik makes a tuple
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#Mixing positional and arbitrary arguments

def make_pizza(size, *toppings):
    print('\nMaking a '+str(size)+" inch pizza with the following toppings: ")
    for topping in toppings:
        print('- '+topping)

make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Using arbitrary keyword arguments
#The doble asterik helps create a dictionary with key pair values
def build_profile(first, last, **user_info):
    profile={}
    profile['first name']=first
    profile['last name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

user_profile=build_profile('albert','einstein',location='princeton',field='physics')

print(user_profile)

#Importing an entire module
""" Importting a module. A module means a file ending in .py
    You can call them by the word inport for example if the file is pizza.py
    then you can import them by import pizza
    after that you need '.' to access the function in the file. For example if the
    for example piiza.make_pizza(arguments), you can also import only the one that you need
    for example from pizza omport make_pizza, then you can directly use the function my itself.
    
    You can also give alias
        eg:- from pizza import make_pizza as mp
        
    If you want to import all the functions, you can
    from pizza import *
    
    Things about styling a function
    Use names that help the user get the hold of the idea of a function parameter
    If you have a default value , there should be no spaces either side of the equal sign
    Comment should be right after the function definition.
    every line should be less than 79 characters, if the function has more parameters, press enter to change line
    """