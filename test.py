# # # # # print("Hello World!!!!")
# # # # a=5 #Instantiate a variable a with value 5
# # # # b=10 #Instantiate a variable b with value 10
# # # # sum=a+b #Add the values of a and b and store the result in sum
# # # # print(sum) #Print the value of sum

# # # # Conditional Programming in Python
# # # a=10
# # # b=-20
# # # if a < 0:
# # #     print("a is negative")
# # # if b < 0:
# # #     print("b is negative")
# # # else:
# # #     print(a+b)

# # a=input("Enter a number: ")
# # b=input("Enter another number: ")
# # if int(a) < 0:
# #     print("a is negative")
# # if int(b) < 0:
# #     print("b is negative")
# # else:
# #    print(int(a)+int(b))
# #    print(f"The sum of {a} and {b} is {int(a)+int(b)}")  

# match_result = input("Enter the match result: ")
# # if match_result == "win":
# #     print("You won the match")
# # elif match_result == "loss":
# #     print("You lost the match")
# # else:
# #     print("The match was a draw")
# match match_result: # available in python 3.10 and above
#     case "win": # case is a keyword used to match the value of match_result
#         print("You won the match")
#     case "loss": # case is a keyword used to match the value of match_result
#         print("You lost the match")
#     case "draw": # case is a keyword used to match the value of match_result
#         print("The match was a draw")
#     case _: # case is a keyword used to match the value of match_result
#         print("Invalid match result")

# Functions aka Methods in Python:
# y=f(x)
# y = dependent variable
# x = independent variable
# f = function

# Area if Rectangle
# Area = f(length,breadth) = length * breadth
# y = Area(length,breadth) = length * breadth
# length = independent variable
# breadth = independent variable
# Area = dependent variable
# f = function

# Area of Rectangle = length * breadth
# Area of Rectangle = f(length,breadth) = length * breadth
# Area of Rectangle = f(length,breadth) = length * breadth
# lenght*breadth = definition of the function

# #  create a function to calculate the area of a rectangle
# def area_of_rectangle(length,breadth):
#     return length * breadth

# print(area_of_rectangle(10,20)) # calling the function
# print(f"The area of the rectangle is {area_of_rectangle(-10,-20)}") # calling the function with negative values

# GLOBAL AND LOCAL VARIABLES IN PYTHON:
# Global variables are variables that are defined outside of a function and can be accessed by any function in the program.
# Local variables are variables that are defined inside a function and can be accessed only by that function.
# Error Type 1 we can solve is called Exception
# Error Type 2 we cannot solve is called Error

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# try:
#     result = a/b
# print(result)
# except Exception as e:
#     print(f"Error: e")

