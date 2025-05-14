# def evennums(num):
#     if num == 2:
#         print(2)
#         return num
#     else:
#         print(num)
#         return evennums(num-2)
#         print ("hi")
# print(evennums(6
#                ))
# '''
# a = int(input())
# def fib(i):
#     if i <= 1:
#         return i
#     else:
#         b = fib(i-1) + fib(i-2)
#         print (b)
#         return b
#
# print(fib(a))

# a = int(input())
# def factorial(i):
#     if i <= 1:
#         return 1
#     else:
#         b = i*factorial(i-1)
#         print (b)
#         return b
#
# print(factorial(a))

# def sumlist(num):
#     if num == 1:
#         return 1
#     else:
#         b = num+sumlist(num-1)
#         print(b)
#         return b
# print(sumlist(8))

# def fac(num):
#     if num == 1:
#         return 1
#     else:
#         return num*fac(num-1)
#

# def sumd(num):
#     i = int(str(num[0]))
#     if len(str(num)) == 1
#         print(num)
#     else:
#         print(i)
# Define a function named sumDigits that calculates the sum of the digits of a given number 'n'
# def sumDigits(n):
#     # Check if 'n' is 0 (base case for summing digits)
#     if n == 0:
#         # If 'n' is 0, return 0 (no digits to sum)
#         return 0
#     else:
#         # If 'n' is not 0, calculate the sum of the last digit (n % 10) and
#         # recursively call the sumDigits function on the remaining digits (n / 10)
#         return n % 10 + sumDigits(int(n / 10))
#
# # Print the result of calling the sumDigits function with the input value 345
# print(sumDigits(100))
#
# # Print the result of calling the sumDigits function with the input value 45
# print(sumDigits(45))
# n = int(input())
# def harm(num):
#     if num == 1:
#         return 1
#     else:
#         return 1/num + harm(num-1)
#
# print(harm(n))