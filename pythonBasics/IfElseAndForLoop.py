greeting = 'Good Morning'
a = 4

if greeting == 'Good Morning':
    print('Condition Matched')
    print('Second Line')
else:
    print('Condition don`t Matched')

print('If Else condition is Completed')

#For Loop

listValues = [2, 3, 5, 7, 9]
for i in listValues:
    print(i*2)

# Sum of First five Natural Number 1+2+3+4+5 = 15
# rang(i.j) --> i to j-1
sumNumber = 0
for j in range(1, 6):
    sumNumber = sumNumber + j
print(sumNumber)

print('Saprate Value')
for k in range(1, 10, 5):
    print(k)

print('Saprate Value')
for m in range(10):
    print(m)
