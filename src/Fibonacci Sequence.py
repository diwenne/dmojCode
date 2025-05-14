import time
# def matrix_multiply(A, B):
#
#     result = [[0, 0], [0, 0]]
#     for i in range(2):
#         for j in range(2):
#             for k in range(2):
#                 result[i][j] += A[i][k] * B[k][j]
#     return result
#
#
# def matrix_power(matrix, n):
#     result = [[1, 0], [0, 1]]
#     while n > 0:
#         if n & 1:
#             result = matrix_multiply(result, matrix)
#         matrix = matrix_multiply(matrix, matrix)
#         n >>= 1
#     return result
#
#
# def fibonacci(n):
#
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#
#
#     fib_matrix = [[1, 1],
#                   [1, 0]]
#
#
#     result_matrix = matrix_power(fib_matrix, n - 1)
#
#
#     return result_matrix[0][0]
#
#
# n = int(input())
# print(fibonacci(n)%(10**9+7))
MOD = 1000000007


def mat_mult(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
         (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
         (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]


def mat_pow(A, n):
    result = [[1, 0], [0, 1]]  # Identity matrix
    base = A

    while n > 0:
        if n & 1:
            result = mat_mult(result, base)
        base = mat_mult(base, base)
        n >>= 1

    return result


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    F = [[1, 1], [1, 0]]

    result_matrix = mat_pow(F, n - 1)

    return result_matrix[0][0]


# Input
n = int(input())
print(fibonacci(n))
