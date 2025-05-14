n = int(input())
if n == 1 or n == 9 or n == 10:
    print(1)
elif n == 2 or n == 3 or n == 7 or n == 8:
    print(2)
elif n == 4 or n == 5 or n == 6:
    print(3)

# n = int(input())
# counter = 0
# for i in range(n):
#     counter +=1
#     x = n - i
#     if x == i:
#         break
#     elif x == i+1:
#         break
#     elif counter == 5:
#         break
# print(counter)







# 1: 1
# 2: 2
# 3: 3, 2 1
# 4: 4, 3 1, 2 2
# 5: 5, 4 1, 3 2,
# 6: 6, 5 1, 4 2, 3 3
# 7: 7, 6 1, 5 2, 4 3,
# 8: 8, 7 1, 6 2, 5 3, 4 4
# 9: 9, 8 1, 7 2, 6 3, 5 4
# 10: 10, 92, 83, 74, 64 55