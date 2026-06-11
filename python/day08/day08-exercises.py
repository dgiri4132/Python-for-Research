#Try it yourself

#9-1
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    
    def describe_restaurant(self):
       print("The restaurant's name is "+ self.restaurant_name.title() + " .")
       print("The restaurant's cuisine type is " + self.cuisine_type.title() + ".") 
    
    def open_restaurant(self):
        print("The restaurant is open.")
    

Bharbay=Restaurant("Bharbay", "momo")
Bharbay.describe_restaurant()
Bharbay.open_restaurant()