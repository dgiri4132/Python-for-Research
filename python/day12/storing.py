#using json.dump() and json.load()

import json

username = input("What is you name? ")

filename='username.json'
try:
    with open('python/day12/'+filename) as f_obj:
        json.load(f_obj)
except FileNotFoundError:
        username=input("What is your name? ")
        with open(filename,'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
else:
     print("Welcome back, "+ username + "!")

