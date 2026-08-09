import json
from country_codes import get_country_code
import pygal_maps_world.maps as mp
from pygal.style import RotateStyle

filename = 'python/chapter16/gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)
cc_gdp = {}
cc_gdp_1, cc_gdp_2, cc_gdp_3 = {}, {}, {}
for pop_dict in gdp_data:
    if pop_dict['Year'] == 2010:
        country_name = pop_dict['Country Name']
        gdp = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_gdp[code] = gdp
for cc, gdp in cc_gdp.items():
    if gdp < 100000000000:
        cc_gdp_1[cc] = gdp
    elif gdp < 5000000000000:
        cc_gdp_2[cc] = gdp
    else:
        cc_gdp_3[cc] = gdp
print(len(cc_gdp_1), len(cc_gdp_2), len(cc_gdp_3))

wm_style = RotateStyle('#336699')
wm = mp.World()
wm.title = 'World Population in 2010, by Country'
wm.add('0-100bn', cc_gdp_1)
wm.add('100bn-5trn', cc_gdp_2)
wm.add('>5trn', cc_gdp_3)
wm.render_in_browser()