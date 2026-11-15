# # # #Arrays - A sequence of elements of the same type 
# # # Arrays are fixed type
# # # Arrays are homogenous
# # # In Python: 
# # # Arrays are not directly accessible to the developer in python, you have to use Lists

# # # # list 
# # # # List is dynamic Array 
# # # import sys
# # Tuple
# # A tuple is like a list. But it is immutable.


# L1 = [10,20,30,40,50]
# print(L1)
# print(sys.getsizeof(L1))

# # # total_size = sys.getsizeof(L1) + sum(sys.getsizeof(item) for item in L1)
# # # print(total_size)  # Outputs: 244 bytes (104 + 5 * 28)

# # # # Linked List is comprised on nodes> nodes has 2 parts : data and pointer of next node

# # # # constructor to initialize a new node with data
# # # class Node:
# # #     def __init__(self, new_data):
# # #         self.data = new_data
# # #         self.next = None

# # # # Create the first node (head of the list)
# # # head = Node(10)

# # # # Link the second node
# # # head.next = Node(20)

# # # # Link the third node
# # # head.next.next = Node(30)

# # # # Link the fourth node
# # # head.next.next.next = Node(40)

# # # # printing linked list
# # # temp = head
# # # while temp is not None:
# # #     print(temp.data, end=" ")
# # #     temp = temp.next

# # import sys

# # class Node:
# #     def __init__(self, new_data):
# #         self.data = new_data
# #         self.next = None

# # # Create the linked list
# # head = Node(10)
# # head.next = Node(20)
# # head.next.next = Node(30)
# # head.next.next.next = Node(40)

# # def get_linked_list_size(head):
# #     total_bytes = 0
# #     seen_ids = set()  # Prevents double-counting shared data objects
# #     temp = head

# #     while temp is not None:
# #         # 1. Size of the Node object itself (48 bytes)
# #         total_bytes += sys.getsizeof(temp)
        
# #         # 2. Size of the Node's internal __dict__ storing 'data' and 'next' (104 bytes)
# #         if hasattr(temp, '__dict__'):
# #             total_bytes += sys.getsizeof(temp.__dict__)
            
# #         # 3. Size of the actual data (28 bytes per int), counted once per unique object
# #         if id(temp.data) not in seen_ids:
# #             total_bytes += sys.getsizeof(temp.data)
# #             seen_ids.add(id(temp.data))
            
# #         temp = temp.next

# #     return total_bytes

# # print("Total Linked List Memory:", get_linked_list_size(head), "bytes")

# import sys

# class Node:
#     def __init__(self, new_data):
#         self.data = new_data
#         self.next = None

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)

# # Calculate memory of ONLY the data values
# data_memory = 0
# temp = head

# while temp is not None:
#     data_memory += sys.getsizeof(temp.data)
#     temp = temp.next

# print("Data-only memory:", data_memory, "bytes")

my_tuple = ("Ankush", True, 1, 3, 4 , [6,7,8])
#my_tuple[1] = "Shantanu"
print(my_tuple)
# Stack 
# VIP from data structures perspectives Recursion 
# LIFO: last in First Out
stack = []  # stack = list()
stack.append(10)
stack.append(20)
stack.append(-10)
print(stack)
stack.pop(1)
print(stack)

# Queue
#First in first OUT
# Removal from left, addition from Right
# breadth for search in data structures, Tree, traversal, pre, post 
# queue also is workable via list()

# Set
# A set is like a list, but cannot contain duplicates. It is unordered.
my_set = {"Akansha","Vipul", 1, 2} # myset={}
print(my_set)
a = set()

# Given 2 strings, tell me if they are using the same alphabets(assuming each alphabet only appears once in each string)

# internal workings of a set