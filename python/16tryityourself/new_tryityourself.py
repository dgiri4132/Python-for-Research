import csv
import pygal_maps_world.maps as mp
from pygal_maps_world.i18n import COUNTRIES
import pycountry

def alpha3_to_alpha2(alpha3_code):
     country  = pycountry.countries.get(alpha_3 = alpha3_code)
     return country.alpha_2.lower() if country else None


filename = 'python/16tryityourself/Electricity.csv'

with open(filename) as  f:
    reader = csv.reader(f)
    next(reader)
    next(reader)
    next(reader)
    next(reader)

    j = 0
    ee={}
    for i,value in enumerate(next(reader)):
        if value == "2023":
            j=i
            break
    for row in reader:
        country_code_1 = row[1]
        ee_data = row[j]
        if ee_data:
            country_code = alpha3_to_alpha2(country_code_1)
            if country_code:
                ee[country_code] = float(ee_data)
tier_1,tier_2,tier_3 = {},{},{}
for cn,per in ee.items():
    if float(per)>90:
        tier_1[cn] = per
    elif float(per) >60:
        tier_2[cn] = per
    else:
        tier_3[cn] = per


wm = mp.World()
wm.title = 'Electricity Accesibility by Country'
wm.add('>90', tier_1)
wm.add('90-60', tier_2)
wm.add('<60', tier_3)
wm.render_in_browser()

    