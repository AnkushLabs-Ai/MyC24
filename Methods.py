# # Functions That Belong to Objects
# # Objects have data (attributes). But real objects also do things. A User can log in. An Order can calculate its total. A Rectangle can compute its area. Methods are functions defined inside a class that give objects behavior.
# class User:
#     def __init__(self,name):
#         self.name =name

#     def greet(self):
#             return f"Hello, I'm {self.name}"

# user = User("Ankush")
# print(user.greet())

# from turtle import width


# class Rectangle:
#     def __init__(self, width, height):
#         self.width =width
#         self.height = height

#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2* (self.width + self.height)

# rect = Rectangle(10,5)
# # print(rect.area())
# # print(rect.perimeter())

# class Rectangle:
#     def __init__(self, width):
#         self.width = width

#     def resize(self, width):
#         self.width = width

# rect = Rectangle(5)
# rect.resize(10)
# print(rect.width)

# def area(a, b):
#     return a * b

# print(area(5,10))

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        return self.balance


account = BankAccount(100)

account.deposit(50)
print(account.show_balance())  

account.withdraw(30)
print(account.show_balance())