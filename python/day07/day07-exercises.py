#Lets start with exercises

def show_magicians(magician_list):
    for magician in magician_list:
        print(magician)
def make_great(magician_list):
    for magician in magician_list:
        print("Great "+ magician)

magicians=['John','David','Phil','Luke']
show_magicians(magicians)
make_great(magicians)


#8-14

def car_info(manufacturer, model, **more_car_info):
    car_profile={}
    car_profile['manufacturer']=manufacturer
    car_profile['model']=model
    for key,values in more_car_info.items():
        car_profile[key]=values
    return car_profile

car=car_info('subaru','outback',color='blue', tow_package=True)
print(car)
