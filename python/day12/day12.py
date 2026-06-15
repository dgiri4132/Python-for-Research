"""
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

birthday= input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print('your birthday appears in the first 300 digits of pi!.')
else:
    print('Your birthday does not appear in the first 300 digits of pi.')

# Writing to a file
with open('python/day11/experiment.txt','w') as experiment:
    experiment.write("I love programming.\n")
    experiment.write('I love creating new games.\n')

with open('python/day11/experiment.txt','a') as experiments:
    experiments.write("I also love finding meaning in large datasets\n")
    experiments.write('I love creating apps that can run in a browser.\n')

#Exceptions
 Exceptions are used to manage errors that arise during a program's execution."""
 

#Handling the FileNotFoundError Exception


# here the current error is FileNotFoundError
# So we add try except method to it

#Analyzing text
# The split method separates a string into parts whereever it finds a space and stores all the parts of the
# string in a list
def count_words(filename):
    try:
        with open('python/day12/'+filename) as f_obj:
            contents= f_obj.read()
# For not reporting every exception you can just write pass as well
    except FileNotFoundError:
        pass
    else:
        words=contents.split()
        num_words = len(words)
        print("The file "+ filename + " has about " + str(num_words) + " words.")

filenames=['experiment.txt','siddhartha.txt','learning_python.txt']
for filenamed in filenames:
     count_words(filenamed)
