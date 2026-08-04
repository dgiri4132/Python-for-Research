import csv
import matplotlib.pyplot as plt
import datetime as datetime
filenames = ['python/16tryityourself/death_valley_2014.csv', 'python/16tryityourself/sf_weather_2014.csv','python/16tryityourself/sitka_weather_2014.csv']
list_names = ["death_valley", "san_francisco", "sitika"]
data = {}
for places, filename in zip(list_names, filenames):
    dates, highs, lows = [], [], []
    with open (filename) as d:
        reader = csv.reader(d)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[2])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

        data[places] = {'dates': dates, 'highs' : highs, 'lows': lows}
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.title("Mean temperatures of Death Valley, San Francisco and Sitika")
plt.plot(data[list_names[0]]['dates'], data[list_names[0]]['highs'], c = 'red', alpha = 0.8, label = 'Death Valley' )
plt.plot(data[list_names[1]]['dates'], data[list_names[1]]['highs'], c = 'blue', alpha = 0.8, label = 'San Francisco')
plt.plot(data[list_names[2]]['dates'], data[list_names[2]]['highs'], c = 'green', alpha = 0.8, label = 'Sitika' )
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)
plt.legend()
plt.show()
        
