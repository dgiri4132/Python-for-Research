# day 03 starts

#Boolean expressions
# it is just true or false, also covered in the exercises just now

# if-statements
age=19
if age>=18:
    print("You are old enough to vote!")
    print('Have you registered to vote yet?')
# if-else statements
else:
    print('Sorry, you are too young to vote.')
    print('Please register to vote as soon as you turn 18!')

# use else block carefully and it matches any condition that wasn't matched by a specific if or elif
# if sometimes you need to check all of the conditons, better to use many ifs rather than elifs
# eg
requested_toppings=['mushrooms','extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print("\nFinished making your pizza! ")

#cheking that a list is not empty

requested_toppings=[]

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print('Sorry we are out of green peppers right now.')
        else:
         print('Adding '+ requested_topping + '.')

    print('\nFinished making your pizza.')
else:
    print('Are you sure you want a plain pizza?')

# Chapter 6 Dictionaries

alien_0={'color':'green', 'points':5}

print(alien_0['color'])
print(alien_0['points'])

#adding values to a dictionary

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Modifying is easy
alien_0['color']='yellow'

# incrementing values 
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

if alien_0['speed']=='slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position']= alien_0['x_position']+x_increment

print("Noew x-position:" +str(alien_0['x_position']))
