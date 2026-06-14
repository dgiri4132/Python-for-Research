# Exercises
#10-6
"""try:
    first=int(input("Enter the first number: "))
    second=int(input("Enter the second number: "))
    sum= first+second
    print(sum)
except ValueError:
    print(" Sorry one of the inputs is not a number.")"""
#Input will always put out value error , if you want type you need to have a list, no input from terminal for it to be a type
try:
    with open('python/day12/cats.txt','w') as f_obj:
        f_obj.write('Smirk\n')
        f_obj.write('Lilly\n')
        f_obj.write('Leila\n')

    with open('python/day12/dogs.txt','w') as f_obj:
        f_obj.write('daniel\n')
        f_obj.write('De vito\n')
        f_obj.write('carry\n')
except FileNotFoundError:
    print(" Sorry There is no file like that")