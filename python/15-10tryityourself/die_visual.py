from die import Die
import pygal
import matplotlib.pyplot as plt

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)


plt.figure(figsize = (12,8))
plt.hist(results, bins = range(2,14), align = 'left', edgecolor = 'black')
plt.xticks(range(2,13))
plt.show()