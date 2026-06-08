#Exercises

#7-1 Rental Car:
question=input("What kind of rental car you would like? ")
print("Let me see if I can find you a "+question.title())

#7-2
table=input(int("How many people are in your dinner group? "))

if table>8:
    print(" Sorry. You'll have to wait. ")
else:
    print('Your table is ready. ')


#7-2
prompt=" Enter all the toppings an enter quit when you are finished"

while True:
    message=input(prompt)
    if message== 'quit':
        break
    else:
        print(message)

#7-5
prompt=input(int(" Please tell you age: "))

if prompt<3:
    print("The ticket is free")
elif prompt>3 and prompt<12:
    print("The ticket is $10")
else:
    print('The ticket is $15')


#7-8
sandwich_orders=['tune sandwich','chicken sandwich','pork sandwich','ranch sandwich']

finished_sandwich=[]

while sandwich_orders:
    recently_finished= sandwich_orders.pop(1)

    print('I namde your '+recently_finished)

    finished_sandwich.append(recently_finished)

print("------- Sandwich List-------\n")
for sandwich in finished_sandwich:
    print(sandwich+'\n')


