# day 04
#Removing key-value pair

alien_0={'color':'green', 'points':5}

del alien_0['points']

print(alien_0)

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print("Sarah's favorite language is "+ favorite_languages['sarah'].title()+'.')

user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key,value in user_0.items():
    print("\nKey: "+ key)
    print("Value: "+ value)


for key in sorted(user_0.keys()):
    print(key)

for values in user_0.values():
    print(values)

for values in set(favorite_languages.values()):
    print(values)

#A list of Dictionaries

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens=[alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# adding or creating lists of dictionaries

aliens=[]
for alien_number in range(30):
    new_alien={'color': 'green', 'points': 5}
    aliens.append(new_alien)


print(aliens[:3])

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10


# A list in a dictionary
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
print('You ordered a '+ pizza['crust'] + "-crust pizza"+" with the following toppings:")

for topping in pizza['toppings']:
    print("\t"+topping)

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite languages are: ")
    for language in languages:
        print('\t'+ language.title())

users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}

for username, user_info in users.items():
    print("\nUsername: "+ username)
    full_name=user_info['first']+" "+ user_info['last']
    location=user_info['location']

    print('\tFull name: '+full_name.title())
    print('\tlocation: ' + location.title())
