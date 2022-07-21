file = open('test.txt')
# Read all the contents of file

# Read n numbers of characters by passing parameters
# print(file.read(9))

# Read one single line at a time readline()
# print(file.readline())
# print(file.readline())

# Print line by line using readline method
# line = file.readline()
# while line != '':
#     print(line)
#     line = file.readline()

for line in file.readlines():
    print(line)

file.close()
