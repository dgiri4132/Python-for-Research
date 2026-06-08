#Chapter 7
# Everything is basic as usual, compring values, taking inputs and stuff

# Letting the user choose whenn to quit

prompt="\n Tell me something, and I will repeat it back to you: "
prompt+="\n Enter 'quit' to end the program"

message=""
while message != 'quit':
    message = input(prompt)

    if message!='quit':
        print(message)


# Using a flag 

prompt="\n Tell me something, and I will repeat it back to you: "
prompt+="\n Enter 'quit' to end the program"

active=True
while active:
    message=input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to exit a loop

prompt="\n Tell me something, and I will repeat it back to you: "
prompt+="\n Enter 'quit' to end the program"

active=True
while active:
    message=input(prompt)

    if message == 'quit':
        break # A loop that starts with while True will run forever unless it reaches a break statement
    else:
        print(message)

# Using continue in a Loop

current_number=0
while current_number < 10:
    current_number+=1
    if current_number %2==0:
        continue
    print(current_number)


# Using a while loop with lists and dictionaries

unconfirmed_users=['alice','brian','candace']
confirmed_users=[]

while unconfirmed_users:
    confirmed_users.append(unconfirmed_users[0])
    print("Verifying user: "+ confirmed_users[-1].title())
    del unconfirmed_users[0]


#Removing all Instances of Specific Values from a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a dictionary with user Input

responses={}

polling_active=True
while polling_active:
    name=input('\nWhat is your name ?')
    response= input('\n Which mountain would you like to climb ?')

    responses[name]=response

    repeat=input("Would you like to let another person respond ?(yes/no)")
    if repeat == 'no':
        polling_active=False

for name, response in responses.items():
    print(name + " would like to climb "+response+".")
    