# 9-4
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=12
    
    def describe_restaurant(self):
       print("The restaurant's name is "+ self.restaurant_name.title() + " .")
       print("The restaurant's cuisine type is " + self.cuisine_type.title() + ".") 
    
    def open_restaurant(self):
        print("The restaurant is open.")
    
    def increment_number_served(self,number):
        self.number_served+=number
    
restaurant=Restaurant('bharbay','momo')
print(restaurant.number_served)
restaurant.increment_number_served(20)
print(restaurant.number_served)

#9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=['Vanilla','Chocolate','Fuck this shit']

    def show_flavors(self):
        print("\nThe flavors are: ")
        for i in range(0,len(self.flavors)):
            print(self.flavors[i])

ice_cream_stand=IceCreamStand('bharbhay','momo')
ice_cream_stand.show_flavors()