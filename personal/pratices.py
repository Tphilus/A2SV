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
"""
count = 0
while count != 6:
    print(count)
    count += 1
