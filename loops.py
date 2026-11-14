# total = 0
# for i in range(1, 4):
#     total += i
# print(total)
# fruits = ["apple", "banana", "cherry"]

# # Without enumerate (works but clunky)
# for i in range(len(fruits)):
#     print(f"{i}: {fruits[i]}")

# # With enumerate (cleaner)
# for i, fruit in enumerate(fruits):
#     print(f"{i}: {fruit}")

# # Start from a different number
# for i, fruit in enumerate(fruits, start=-2):
#     print(f"{i}: {fruit}")
# # 1: apple, 2: banana, 3: cherry

# # Multiplication table
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")
#     print("---")

# numbers = [1, 2, 3, 4, 5]
# cubes = []

# for n in numbers:
#     cubes.append(n ** 3)

# print(cubes)

# for i in range(3): print(i, end=" ")

# while True:
#     age = input("Enter your age: ")

#     if age.isdigit() and int(age) > 0:
#         age = int(age)
#         break  # Exit the loop

#     print("Please enter a valid positive number.")

# print(f"Your age is {age}")

# x = 10
# while x > 0:
#     x -= 3
#     print(x)

# tasks = ["email", "backup", "report"]

# while tasks:  # Non-empty list is truthy
#     current = tasks.pop(0)  # Remove first item
#     print(f"Processing: {current}")

# print("All tasks complete!")

# import time

# status = "pending"
# checks = 0

# while status != "complete" and checks < 10:
#     print(f"Checking status... ({checks + 1})")
#     # In real code: status = check_api_status()
#     checks += 1
#     time.sleep(1)  # Wait 1 second

# if status == "complete":
#     print("Task completed!")
# else:
#     print("Timed out waiting for completion")

# items = [1, 2, 3] 
# while items: print(items.pop())

# # break — exit the loop immediately
# for n in range(10):
#     if n == 5:
#         break  # Stop here
#     print(n)  # 0, 1, 2, 3, 4

# # continue — skip to next iteration
# for n in range(5):
#     if n == 2:
#         continue  # Skip this one
#     print(n)  # 0, 1, 3, 4

# # else — runs if loop completed without break
# for n in range(3):
#     print(n)
# else:
#     print("Loop finished!")  # This runs

# # Process only valid items
# data = [10, -5, 20, None, 30, "invalid"]

# for item in data:
#     if not isinstance(item, int) or item < 0:
#         continue  # Skip invalid items

#     print(f"Processing: {item}")

# for i in range(5):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)

# Search for a user
# users = ["alice", "bob", "charlie"]
# target = "bob"

# for user in users:
#     if user == target:
#         print(f"Found {target}!")
#         break
# else:
#     print(f"{target} not found")

# # Output: david not found

# for i in range(3):
#     for j in range(3):
#         if j == 1:
#             break  # Only exits inner loop
#         print(f"i={i}, j={j}")
#     print(f"Finished inner loop for i={i}")

# for n in [2, 4, 6]:
#     if n % 2 != 0:
#         break
# else:
#     print("All even!")