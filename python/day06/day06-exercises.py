# City-names

def city_country(city, country):
    complete=city.title()+", "+country.title()
    return complete

pcity=input("Please input your city: \n")
pcountry=input("Please, input your country: ")

print(city_country(pcity,pcountry))
