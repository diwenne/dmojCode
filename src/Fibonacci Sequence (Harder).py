import time

start_time = time.time()  # record the start time
# MOD = 1000000007
# PISANO_PERIOD = MOD - 1  # Pisano period for MOD = 10^9 + 7
#
#
# def mat_mult(A, B):
#     # Multiplies two 2x2 matrices under modulo MOD
#     return [
#         [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
#          (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
#         [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
#          (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
#     ]
#
#
# def mat_pow(A, n):
#     # Matrix exponentiation (A^n) under modulo MOD
#     result = [[1, 0], [0, 1]]  # Identity matrix
#     base = A
#
#     while n > 0:
#         if n & 1:
#             result = mat_mult(result, base)
#         base = mat_mult(base, base)
#         n >>= 1
#
#     return result
#
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#
#     # Base transformation matrix for Fibonacci sequence
#     F = [[1, 1], [1, 0]]
#
#     # We want the (n-1)th power of F
#     result_matrix = mat_pow(F, n - 1)
#
#     # The Fibonacci number will be at position result_matrix[0][0] (F(n))
#     return result_matrix[0][0]
#
#
# def reduce_large_number(num_str, mod):
#     result = 0
#     for digit in num_str:
#         result = (result * 10 + int(digit)) % mod
#     return result
#
#
# # Input: the very large number N as a string
# N = input()
#
# # Step 1: Reduce N modulo the Pisano period (PISANO_PERIOD)
# reduced_n = reduce_large_number(N, PISANO_PERIOD)
# print(reduced_n)
# # Step 2: Compute Fibonacci of the reduced N modulo MOD
# result = fibonacci(reduced_n)
#
# # Output the result
# # print(result)
# #
# MOD = 1000000007
# PISANO_PERIOD = MOD - 1  # Pisano period for MOD = 10^9 + 7
#
#
# def mat_mult(A, B):
#     return [
#         [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
#          (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
#         [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
#          (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
#     ]
#
# def mat_pow(A, n):
#     result = [[1, 0], [0, 1]]  # Identity matrix
#     base = A
#
#     while n > 0:
#         if n & 1:
#             result = mat_mult(result, base)
#         base = mat_mult(base, base)
#         n >>= 1
#
#     return result
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#
#     F = [[1, 1], [1, 0]]
#     result_matrix = mat_pow(F, n - 1)
#
#     return result_matrix[0][0]
#
# def reduce_large_number(num_str, mod):
#     result = 0
#     for digit in num_str:
#         result = (result * 10 + int(digit)) % mod
#     return result
#
# # Read input as string (not integer!)
# n = input().strip()
#
# reduced_n = reduce_large_number(n, PISANO_PERIOD)
# print(fibonacci(reduced_n))
MOD = 10**9 + 7

def mat_mult(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
         (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
         (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def mat_pow(matrix, n_str):
    result = [[1, 0], [0, 1]]  # Identity matrix

    while n_str != "0":
        if int(n_str[-1]) % 2 == 1:
            result = mat_mult(result, matrix)
        matrix = mat_mult(matrix, matrix)
        n_str = divide_by_2(n_str)

    return result

def divide_by_2(n_str):
    result = ""
    carry = 0
    for c in n_str:
        num = carry * 10 + int(c)
        result += str(num // 2)
        carry = num % 2
    return result.lstrip('0') or '0'

def fibonacci(n_str):
    if n_str == "0":
        return 0
    if n_str == "1":
        return 1

    F = [[1, 1], [1, 0]]
    result_matrix = mat_pow(F, str(int(n_str) - 1))
    return result_matrix[0][0]

n = input().strip()
print(fibonacci(n))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.6f} seconds")