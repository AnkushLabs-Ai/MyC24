# # # # # # # # # # # # This RETURNS a value
# # # # # # # # # # # def add_return(a, b):
# # # # # # # # # # #     print("I'm in return statement")
# # # # # # # # # # #     return a + b

# # # # # # # # # # # # This PRINTS a value
# # # # # # # # # # # def add_print(a, b):
# # # # # # # # # # #     print("I am in Print statement")
# # # # # # # # # # #     print(a + b)

# # # # # # # # # # # # With return, you can use the result
# # # # # # # # # # # x = add_return(2, 3)
# # # # # # # # # # # print(x * 2)  # 10

# # # # # # # # # # # # With print, you can't
# # # # # # # # # # # y = add_print(2, 3)  # Prints "5"
# # # # # # # # # # # print(y * 2)         # Error! y is None

# # # # # # # # # # def greet(name):
# # # # # # # # # #     print(f"Hello, {name}!")
# # # # # # # # # #     return name

# # # # # # # # # # result = greet("Alice")  # Prints "Hello, Alice!"
# # # # # # # # # # print(result)            # None

# # # # # # # # # def process_user(user):
# # # # # # # # #     if not user:
# # # # # # # # #         return "No user provided"

# # # # # # # # #     if not user.is_active:
# # # # # # # # #         return "User is inactive"

# # # # # # # # #     # Main logic here (only runs if checks pass)
# # # # # # # # #     return f"Processing {user.name}"

# # # # # # # # def first_even(numbers):
# # # # # # # #     for n in numbers:
# # # # # # # #         if n % 2 == 0:
# # # # # # # #             return n
# # # # # # # #     return None


# # # # # # # # result = first_even([1, 3, 5, 8, 10])
# # # # # # # # print(result)

# # # # # # # def min_max(numbers):
# # # # # # #     return min(numbers), max(numbers)

# # # # # # # lowest, highest = min_max([3, 3, 4, 3, 5, 9])
# # # # # # # print(f"Range: {lowest} to {highest}")  # Range: 2 to 9

# # # # # # def func_a(x):
# # # # # #     x * 2
# # # # # #     return func_a(3)

# # # # # # def func_b(x):
# # # # # #     return x * 2
# # # # # #     print(func_b(3))
    
# # # # # def check_number(n):
# # # # #     if n > 0:
# # # # #         return "positive"
# # # # #     if n < 0:
# # # # #         return "negative"

# # # # # result = check_number(-0)
# # # # # print(result)

# # # # from os import name


# # # # def get_name(): 
# # # #     return "Alice", "Smith"
# # # #     #name = get_name()[0]
# # # #     #first,last = get_name()
# # # #     first = get_name().first
# # # #     print(first)

# # # # def power(base, exponent=2):
# # # #     return base ** exponent

# # # # print(power(3))
# # # # print(power(2, 3))
# # # # print(power(exponent=5, base=2))

# # # def describe_pet(animal="dog", name="Buddy"):
# # #     describe_pet("dog","buddy") 
# # #     print(f"A {animal} named {name}")

# # # def flexible(*args, **kwargs):
# # #     print(f"Positional: {args}")
# # #     print(f"Keyword: {kwargs}")

# # # flexible(1, 2, 3, name="Alice", active=True)
# # # # Positional: (1, 2, 3)
# # # # Keyword: {'name': 'Alice', 'active': True}

# # def greet(name, Yellow,greeting="Hello",):
# #     print(f"{greeting}, {name},{Yellow}!")

# # options = {"name": "Ankush", "greeting": "Hi, how are you?", "Yellow":"yello"}
# # greet(**options)  # Same as greet(name="Alice", greeting="Hi")
# # # Hi, Alice!

# def log_call(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}")
#         result = func(*args, **kwargs)
#         print(f"Returned: {result}")
#         return result
#     return wrapper

# @log_call
# def add(a, b):
#     return a + b

# add(3, 5)

def func(*args, **kwargs): print(len(args), len(kwargs)) 
func(1, 2, 3, a=4, b=5)