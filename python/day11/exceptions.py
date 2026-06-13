#Exceptions
""" Exceptions are used to manage errors that arise during a program's execution.
They are handled with try-except blocks """

try:
    print(5/0)
except ZeroDivisionError:
    print(" You can't divide by zero.")


print('Give me two numbers and I will divide them. ')
print("Enter 'q' to quit. ")

while True:
    first_number= input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number= input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't divide by 0!")
    else:
        print(answer)