#Functions
#Basic functions

def greet_user(username):
    """ Display a simple greeting"""
    print("Hello, "+username.title() + "!")

greet_user('jesse')
#The username is a parameter and jesse in this case is an argument.

#Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type+ ".")
    print("My "+animal_type +"'s name is "+ pet_name.title()+ ".")

describe_pet('hamster','harry')


# keyword argument
describe_pet(animal_type='hamster',pet_name='harry')

# you can also set default values here
# def decribe_pet(pet_name, animal_type='dog')

# When you use default values, any parameter with a default value needs to be listed after all the parameters that 
# don't have default values. This allows python to continue interpreting positional arguments correctly.

# basic errors and stuff which you know from beginning and have revised as well

#Making an argument optional is the following way

def get_formatted_names(first_name, last_name, middle_name=''):
    if middle_name:
        full_name=first_name + ' '+ middle_name + ' '+ last_name
    else:
        full_name= first_name + ' '+ last_name
    return full_name.title()

while True:
    print('\n Please tell me your name: ')
    print("(enter 'q' at any time to quit)")

    f_name=input("First name: ")
    if f_name == 'q':
        break

    l_name=input('Last name: ')
    if l_name == 'q':
        break

    formatted_name=get_formatted_names(f_name,l_name)
    print("\nHello, "+formatted_name + "!")

def greet_users(names):
    for name in names:
        msg="Hello, "+name.title() + "!"
        print(msg)

usernames=["hannah",'ty','margot']
greet_users(usernames)


#Modifying list by a function
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print("Printing model: "+ current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\n The following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#To prevent a function from modifying a list just copy the function
# i.e. function_names(list_name[:])
