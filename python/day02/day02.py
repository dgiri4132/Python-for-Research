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
