#10-1
with open('python/day11/learning_python.txt') as learning_python:
    contents=learning_python.read()

for i in range(3):
    print(contents)

#10-3
with open('python/day11/guest.txt','w') as guest:
    
    while True:
        name=input(("Please enter your name: "))
        print("Welcome to Ceaser's Palace "+ name)
        print('Enter q to quit')
        if name == 'q':
            break
        guest.write(name+"\n")

