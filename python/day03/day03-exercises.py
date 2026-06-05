# Exercises

#5-1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#5-4
alien_color='green'
if alien_color =='green':
    print( "You've earned 5 points.")

else:   
    print("You've earned 10 points.")

requested_toppings=['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry we are out of green peppers right now.')
    else:
        print('Adding '+ requested_topping + '.')

print('\nFinished making your pizza.')

