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
prompt=" Please tell you age: "

