from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    Name_Exceptions = {'Bolivia': 'bo',
    'Brunei': 'bn',
    'Czechia': 'cz',
    'Democratic Republic of Congo': 'cd',
    'East Timor': 'tl',
    'Eswatini': 'sz',        # pygal's data predates the 2018 rename from Swaziland
    'Iran': 'ir',
    'Laos': 'la',
    'Libya': 'ly',
    'Moldova': 'md',
    'North Korea': 'kp',
    'North Macedonia': 'mk',
    'Palestine': 'ps',
    'Russia': 'ru',
    'South Korea': 'kr',
    'Syria': 'sy',
    'Tanzania': 'tz',
    'Venezuela': 've',
    'Vietnam': 'vn'}
    if country_name in Name_Exceptions:
         return Name_Exceptions[country_name]
    for code, name in COUNTRIES.items():
            if name == country_name:
                return code
    return None
