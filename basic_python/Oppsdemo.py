# class are user defined blueprint or prototype
# sum, multiplication, addition, constant
# method, class variable , instance variable , constructor etc
# objects for your classes

#self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object

class Calculator:
    num = 100 # class variable
    #default constructor
    def __init__(self,a,b):
        print("I am called automatically when object is created")
        self.first_number = a #instance variable
        self.second_number = b
    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.first_number + self.second_number + Calculator.num


obj = Calculator(2,3) #syntax to create objects in python
obj.getData()
print(obj.num)
print(obj.summation())

obj1 = Calculator(4,5) #syntax to create objects in python
obj1.getData()
print(obj1.num)
print(obj1.summation())