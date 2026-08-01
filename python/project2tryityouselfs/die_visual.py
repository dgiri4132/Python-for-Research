from die import Die
import pygal

die_1 = Die(6)
die_2 = Die(6)

results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll() 
    results.append(result)

frequencies = []
max_result = die_1.num_sides * die_2.num_sides 
x_labels=[]
for value in range(1, max_result+1):
    x_labels.append(str(value))
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.x_labels = x_labels
hist.title = "Results of rolling three D6 1000 times."
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_in_browser()