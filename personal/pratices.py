# string = 'EPAT Handbook! '
# print(string.index('o'))
# print(type({'key':'value'})) # dict
# print(type((1,2,3))) # tuple
# print(type({1,2,3}))

# print("Hello " + str(2019))

"""
=============
Chapter 4
Modules, Packages and Libraries
=============
"""

# def addition(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# def division(dividend, dividor):
#     return dividend / dividor

# def factorial(n):
#     i = 0
#     result = 1
#     while i != n:
#         i += 1
#         result *= i
#     return result
# print(factorial(5))

# result = addition(2, 3)
# print(result)

"""
====================
Importing modules
====================
"""

# import math as m # assign it with alias
# import math

# res = math.pi
# res = math.floor
# print(dir(math))

"""
================
Chapter 5
Data Structures
================
"""

# A string can be sequence of characters
# data structures stores sequences of object(float, integers, string, etc).

# sequences = ['a','b','c','d','e','f','g','h','i','j']
# print(sequences[0:])
# print(sequences[:-1])

# ==== Tuple ====

# tup = (1, 2, 4)
# tup2 = (1, "a", 2,.5)
# tup3 = (1,) * 5 # Not trailing comma
# print(tup + tup2) 


"""
==============
Dictionary
==============
"""

# ticker = {'symbol': 'AAPL',
# 'price': 224.95,
# 'company': 'Apple Inc',
# 'founded': 1976,
# 'products': ['Machintosh', 'iPod', 'iPhone', 'iPad']
# }
# ticker['price'] = 222
# del(ticker['company'])
# print(ticker.keys())

"""
==============
Bitwise operator
==============
"""

# andFun = 201 & 15
# orFun = 201 | 15
# xor = 1 ^ 3
# print(andFun)
# print(orFun)
# print(xor)

"""
=============
Control Flow Statements
=============
# """
# count = 0
# while count != 6:
#     print(count)
#     count += 1
"""
while condition expression:
    code statement 1
    code statement 2
    ......
    code statement n

"""

# data_point = 6 
# count = 0

# while count != data_point:
#     print(count)
#     count += 1

"""
for item in sequence:
    code statement 1
    code statement 2
    ......
    code statement n
"""

# top_gainers = ['BHARTIARTL', 'EICHERMOT', 'HCLTECH',
# 'BAJFINANCE', 'RELIANCE']

# for gainer in top_gainers:
#     print(str(top_gainers.index(gainer)) + ' : ' + gainer)

# for i in range(len(top_gainers)):
#     print(i, top_gainers[i])

# for i, val in enumerate(top_gainers):
#     print(i, val)
"""
===============
 Looping through dictionaries
===============
"""
# dict = {'AAPL':193.53,
# 'HP':24.16,
# 'MSFT':108.29,
# 'GOOG':1061.49}

# for key, val in dict.items():
#     print(f"Price of {key} is {val}")

# print(dict.items())

"""
===============
 Nested through 
===============
"""

# for table_val in range(1, 10):
#     for mul in range(1, 11):
#         ans = table_val * mul
#         print(ans, end=" ")
#     print()

# Example 1: Calculating the Average of Numbers
# numbers = [10, 20, 30, 40, 50]
# total = 0

# for num in numbers:
#     total += num

# avg = total // len(numbers)
# print(avg)

# Example 2: Finding the Maximum Value
# numbers = [5, 2, 8, 1, 9]
# max_val = numbers[0]

# this
# for num in numbers:
#     if num > max_val:
#         max_val = num

# print(max_val) 

# Or This 
# for num in numbers:
#     max_val = max(max_val, num)

# print(max_val) 

# Example 3: Reversing a List
# numbers = [1, 2, 3, 4, 5]
# reverse_list = numbers[::-1]
# print(reverse_list)

# Find the min num
# numbers = [5, 2, 8, 1, 9]
# min_val = numbers[0]

# for num in numbers:
#     # if num < min_val:
#     #     min_val = num
#     min_val = min(min_val, num)

# print(min_val)

# numbers = [1, 2, 3, 4, 5]
# count = 0
# count = sum(numbers)

# # for num in numbers:
# #     count += num

# print(count)

# def calculate_prefix_sum(arr):

    # Calculates the prefix sum array for a given array.

    # Args:
    #     arr (list): The input array.

    # Returns:
    #     list: The prefix sum array.
    
    # n = len(arr)
    # prefix_sum = [0] * n
    
    # if n > 0:
    #     prefix_sum[0] = arr[0]

    #     for i in range(1, n):
    #         prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    
    # return prefix_sum

    # ===== Padding with Zeros ===== 
    # prefix_sum = [0]*(n + 1)

    # for i in range(1, n+1):
    #     prefix_sum[i] = arr[i - 1] + prefix_sum[i - 1]
    
    # return prefix_sum

    # Normal
    # prefix_sum = [0] * n
    # curr_sum =  0

    # for i in range(n):
    #     curr_sum += arr[i]
    #     prefix_sum[i] = curr_sum
    
    # return prefix_sum

    # === 
    # prefix_sum = [0] * n
    # prefix_sum[0] = arr[0]

    # for i in range(1, n):
    #     prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    
    # return prefix_sum

# Example usage:
# arr = [1, 2, 3, 4, 5]
# prefix_sum = calculate_prefix_sum(arr)
# print(f"Original array: {arr}")
# print(f"Prefix sum array: {prefix_sum}")


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]b
# ]

# rows = len(matrix)
# cols = len(matrix[0])

# prefix_sum = [[0] * cols for _ in range(rows)]
# print(prefix_sum)


# LinkedList

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# row = len(matrix)
# col = len(matrix[0])

# transposed = [[0]* col for _ in range(row)]
# print(transposed)

# for row_idx in range(len(matrix) -1,-1,-1):
#     for col_idx in range(len(matrix[0]) -1,-1,-1):
#         print(matrix[row_idx][col_idx])

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# num_rows = len(matrix)
# num_cols = len(matrix[0]) # Assuming all rows have the same length

# for j in range(num_cols):  # Iterate through columns
#     for i in range(num_rows):  # Iterate through rows
#         print(matrix[i][j], end=" ")
#     print()  # Newline after each column

"""
=============
Binary Search
============
"""

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low < high:
#         mid = (low + high) // 2

#         if target == arr[mid]:
#             print("Target is found", mid)
#             break
#         elif target > arr[mid]:
#             low = mid + 1 
#         else:
#             high = mid - 1

# arr = [1, 2, 3, 4, 5, 6, 8]
# target = 6
# print(binary_search(arr, target))


# def bisect_left(arr, target):
#     low = 0
#     high = len(arr) -1

#     while low < high:
#         mid = (low + high) // 2
#         if arr[mid] > target:
#             pass


# arr = [1, 2, 3, 4, 5, 6, 8]
# target = 6

# def bisect_right(arr, target):
#     pass

"""
=============
Sliding Window
=============
"""
# s = "banana"
# count = {}

# for char in s:
#     if char not in count:
#         count[char] = 1
#     else:
#         count[char] += 1
# print(count)

# for char in s:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1

# print(count)

s = "aababcabc"
count = 0
i = 0

while i < len(s) - 2:
    window = set(s[i: i + 3])

    if len(window) == 3:
        count += 1
    i += 1

print(count)

class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
    
    def __str__(self):
        return str(self.val)
    
head = Node(1)
A = Node(2)
B = Node(3)
C = Node(4)

head = A
A.next = B
B.next = C
# print(head.next)

# == Traverse Trough
# cur = head
# while cur:
#     print(cur, end=" -> ")
#     cur = cur.next

curr = head
element = []
while curr:
    element.append(str(curr.val))
    curr = curr.next

print(' -> '.join(element))

def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    
    return False

print(search(head, 2))
