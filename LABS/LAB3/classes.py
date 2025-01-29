from math import sqrt
#1
class String():
    def __init__(self):
        self.str = ""
    
    def getString(self):
        self.str = input("Enter a string: ")
    
    def printString(self):
        print(self.str.upper())

str1 = String()
#str1.getString()
#str1.printString()

#2
class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length=0):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length ** 2

#3
class Rectangle(Shape):
    def __init__(self, length=0, width = 0):
        super().__init__()
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width 

shape = Shape()
print("Shape area:", shape.area())
square = Square(4)
print("Square area:", square.area())
rectangle = Rectangle(4, 5)
print("Rectangle area:", rectangle.area())

#4
class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)
    
    def move(self):
        self.x, self.y = input("Enter x coordinate "), input("Enter y coordinate ")
    
    def dist(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

p1, p2 = Point(), Point(3,4)
p1.show()    
p2.show()
print(p1.dist(p2))

#5
class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        self.balance += float(input("Type the amount you want to deposit: "))
    
    def withdraw(self):
        while True:
            amount = float(input("Type the amount you want to withdraw: "))
            if amount > self.balance or amount <= 0:
                print("You have typed incorrect number")
                continue
            else:
                self.balance -= amount
                print("Your money has been successfully withdrawn!")
                break

#user1 = BankAccount("Chip", 120)
#print(user1.balance)
#user1.withdraw()
#print(user1.balance)

#6
list = [i for i in range(101)]
edited_list = filter(lambda n: isprime(n), list)

def isprime(n):
    for i in range(2, n):
        if n%i==0: return 0
    if not (n == 0 or n == 1): return 1

for i in edited_list:
    print(i, end=" ")