#files
#now making lists of lines from a file
with open('python/day11/pi_digits.txt') as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.rstrip())


pi_string=''
for line in lines:
    pi_string+=line.rstrip()

print(pi_string)
print(len(pi_string))


with open('python/day11/pi_till_300.txt') as digits_300:
    lines=digits_300.readlines()
pi_new_string=''
for line in lines:
    pi_new_string+=line.strip()
"""
birthday= input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print('your birthday appears in the first 300 digits of pi!.')
else:
    print('Your birthday does not appear in the first 300 digits of pi.')
"""
# Writing to a file
with open('python/day11/experiment.txt','w') as experiment:
    experiment.write("I love programming.\n")
    experiment.write('I love creating new games.\n')
    