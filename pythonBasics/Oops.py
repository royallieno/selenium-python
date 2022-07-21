# Classes are user defined blueprint or protoype
# sum, multiplication, addition, constant
# methods class variables, instance variables, constructor etc
# objects for your classes
# --------------------------------------------------------------
# self keyword is mandatory for calling variables names into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keywork is not required when you create object

class Calculator:
    num1 = 100
    num2 = 200
    sum = num1 + num2
    # Default Constructor

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print('I am called automatically when object is created')

    def getData(self):
        print('I am now executing as method in class')

    def Summition(self):
        return self.firstNumber + self.secondNumber + Calculator.sum


obj = Calculator(2, 5) #Syntax to create objects in python
obj.getData()
print(obj.num1)
print(obj.Summition())

obj1 = Calculator(5, 10) #Syntax to create objects in python
obj1.getData()
print(obj1.num2)
print(obj1.Summition())
