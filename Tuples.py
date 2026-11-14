# # # # # # Create a tuple
# # # # # point = (10, 20)

# # # # # # Access items (same as lists)
# # # # # print(point[0])  # 10

# # # # # # Tuples are immutable — this would error:
# # # # # # point[0] = 15  # TypeError!
# # # # # Tuple of coordinates
# # # # from calendar import c


# # # # point = (10, 20)

# # # # # Tuple of strings
# # # # colors = ("red", "green", "blue")

# # # # # Single-item tuple needs a trailing comma
# # # # single = (42,)     # This is a tuple
# # # # not_tuple = (42)   # This is just the number 42

# # # # # You can omit parentheses (tuple packing)
# # # # coordinates = 10, 20, 30
# # # # print(type(coordinates))  # <class 'tuple'>
# # # # print(coordinates )
# # # # print(coordinates[0])
# # # # print(coordinates[1])
# # # # print(coordinates[2])
# # # # coordinates[0] = 100
# # # # print(coordinates[0])

# # # colors = ("yellow","red", "green", "blue","black","white")

# # # # print(colors[0])    # "red"
# # # # print(colors[-1])   # "blue"
# # # # print(colors[1:3])  # ("green", "blue")
# # # print(colors[-9])

# # # data = (1, 2, [3, 4])
# # # data[2].append(5)
# # # print(data)

# # # colors = ("yellow","red", ["green"], "blue","black","white")
# # # colors[2].append("gray")
# # # print(colors)

# # frozenset = frozenset([1, 2, 3, 4, 5])
# # print(frozenset.add(6))

# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])

# p = Point(10, 20)
# print(p.x)  # 10
# print(p.y)  # 20
# print(p[0]) # 10 (still works like a tuple)
# p[0] = 15
# print(p)

single = (42,12,"hello")
print(type(single))