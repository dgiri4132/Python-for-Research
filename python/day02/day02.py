#Day 02
favorite_language='python '
print(favorite_language.strip())

# can also use lstrip or rstrip to strip based on the side

# Everything basic multiplication and all that other stuff does not need to be covered I think

age=23
message=f'Happy {age}rd Birthday!'
print(message)

# Lists chapter 3

bicycles = ['trek','cannodale','redline','specialized']
print(bicycles[0])
print(bicycles[0].title())
 # modifying
bicycles[0]='giant'
print(bicycles[0])
#appending
bicycles.append('gitano')
bicycles.insert(0,'gtx')
del bicycles[1]

popped_motorcycle=bicycles.pop()

# can also remove by value

bicycles.insert(3,'gitano')

# sorting
sorted_bicycles=sorted(bicycles)
bicycles.sort()
#need to change to lower case before sorting

# Finding length
len(bicycles)

# Working with lists
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print( "I can't wait to see your next trick, " + magician.title() + ".\n")

# all the basic stuffs like indentation and values need to be kept in place

for value in range(1,5):# prints till and including four only
    print(value)

numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)

squares=[]
for value in range(1,11):
    squares.append(value**2)

digits=[1,23,4,5,6,7,8,9,0]

min(digits)
max(digits)
sum(digits)


#Looping through a slice
players=['charles','martina','michael','florence','eli']

print('Here are the first three paluers on my team:')
for player in players[:3]:
    print(player.title())

#copying a list is easy
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
print("\n My friend's favorite foods are: ")
print(friend_foods)

#Tuples are values that cannot change.
#Looks like a list except you use parentheses instead of square brackets.
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#Looping is the same as in a list
#To modify a tuple, you need to change or redefine the entire the whole tuple.

#Chapter 5 if-statements

cars=['bmw','audi','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        break

