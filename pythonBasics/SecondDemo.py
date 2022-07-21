values = [1, 2, 'Arshad', 4.5, 5]
# List is a data type that allows multiple values and can be different data type

print(values[0])  # 1

print(values[3])  # 4.5

print(values[-1])  # 5

print(values[1:4])  # [2, 'Arshad', 4.5]

values.insert(3, 'Gulnawaz')
print(values)

values.append('LaST One')
print(values)

values[2] = 'ARSHAD'
del values[6]
print(values)

# Tuple = Same as list data type but immutable - Values can not be change or update after declearing it
valTuple = (1, 2, 'Arshad', 4.5, 5)

print(valTuple[1])

#valTuple[2] = 'String'

print(valTuple)

# Dictonary
dic = {'a': 2, 4: 'bcd', 'c': 'Hello Word'}

print(dic['a'])
print(dic[4])

#
emptyDic = {}

emptyDic['firstName'] = 'Gulnawaz'
emptyDic['lastName'] = 'Arshad'
emptyDic['gender'] = 'Male'

print(emptyDic)
print(emptyDic['lastName'])

