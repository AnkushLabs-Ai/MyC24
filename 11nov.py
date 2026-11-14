# # # # # data = {"a": 1, "b": 2}
# # # # # data["c"] = data.get("c", 0) + 1
# # # # # print(data)

# # # # # # user = {"name": "Alice"}

# # # # # # # Add a new key
# # # # # # user["email"] = "alice@example.com"

# # # # # # # Update existing key
# # # # # # user["name"] = "Alice Smith"

# # # # # # # Delete a key
# # # # # # del user["email"]

# # # # # # # Remove and return a value
# # # # # # name = user.pop("name")
# # # # # # print(name)  # "Alice Smith"

# # # # # # # pop with default (no error if missing)
# # # # # # role = user.pop("role", "guest")

# # # # user = {"name": "Alice", "age": 30}

# # # # # Check if key exists
# # # # print("name" in user)     # True
# # # # print("email" in user)     # False
# # # # print("email" not in user) # True
# # # # print(user["name"])
# # # # print(user.get("name"))

# # # user = {"name": "Alice", "age": 30, "role": "admin"}

# # # # Iterate over keys (default)
# # # for key in user:
# # #     print(key)  # name, age, role

# # # # Iterate over values
# # # for value in user.values():
# # #     print(value)  # Alice, 30, admin

# # # # Iterate over both
# # # for key, value in user.items():
# # #     print(f"{key}: {value}")

# # user = {"name": "Alice", "age": 30}

# # # Get all keys
# # print(list(user.keys()))  # ["name", "age"]

# # # Get all values
# # print(list(user.values()))  # ["Alice", 30]

# # # Get key-value pairs as tuples
# # print(list(user.items()))  # [("name", "Alice"), ("age", 30)]

# # # Number of keys
# # print(len(user))  # 2

# # # Merge dictionaries
# # defaults = {"role": "user", "active": True}
# # user.update(defaults)
# # print(user)
# # # user is now {"name": "Alice", "age": 30, "role": "user", "active": True}

# # # Python 3.9+ merge syntax
# # merged = user | defaults  # Creates new dict
# # #print(merged)
# # print("Updated user: ", user)
# # print(len(user))

# #Nested Dictionaries
# users = {
#     "alice": {
#         "email": "alice@example.com",
#         "age": 30
#     },
#     "bob": {
#         "email": "bob@example.com",
#         "age": 25
#     }
# }

# # Access nested values
# users["alice"]["email"]  # "alice@example.com"
# print(users)
# print(users.get("email"))

# print(users.get("charlie", {}).get("email", "N/A"))  # "N/A"

# for value in users.values():
#     print(value)

# for key in users.keys():
#     print(key)

# for key, value in users.items():
#     print(key, value)

# email = users.get("alice",{}).get("email","no email found")
# age = users.get("alice",{}).get("age",0)
# print(email, age)