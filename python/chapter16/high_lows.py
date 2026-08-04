import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename = 'python/chapter16/sitka_weather_2014.csv'

""" You don't always have all the data that you are going to be working with, so 
it is better if you setup a try and else error track, it will be easier to do it"""
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates,highs, lows = [], [], []
    for row in reader:
        try:    
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
                print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)   
            lows.append(low)

fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, highs, c = 'red', alpha = 0.5)
plt.plot(dates, lows, c = 'blue', alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)

plt.title("Daily high  and low temperatures - 2014", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()



"""
To remember arguments for the datetime below is the table

%A      Weekday name, such as Monday
%B      Month name, such as January
%m      Month, as a number (01 to 12)
%d      Day of the month, as a number( 01 to 31)
%Y      Four-digit year, such as 2015
%y      Two-digit year, such as 15
%H      Hour, in 24-hour format(00 to 23)
%I      Hour, in 12-hour format(01 to 12)
%p      AM or PM
%M      Minutes (00 to 59)
%S      Seconds (00 to 61)
"""