#Lets do some exercises now

#4-5
million_numbers=list(range(1,1000001))
total_sum=sum(million_numbers)
print(total_sum)
sum_in=0
for number in million_numbers:
    sum_in+=number
print(sum_in)

#4-6
for i in range(1,20,2):
    print(i)

#4-7
for j in range(3,31,3):
    print(j)

#4-8
for i in range(1,11):
    print(i**3)

cube=[x**3 for x in range(1,11)]
print(cube)

#4-13
foods=('rice', 'chicken','salad','barbeque','momo')

for food in foods:
    print(food)
foods[0]='chowmein'
