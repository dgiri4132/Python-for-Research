#Passing a Arbitrary Number of Arguments
# To pass a random number of arguments, use asterik before the definition parameter
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

