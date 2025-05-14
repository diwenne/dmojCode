import sys
n = int(input())
snows = []
for i in range(n):
    snows.append(list(map(int,input().split())))
# print(snows)
boo = True
aa = []
def snowflake(x, y):
    if x[0] in y:
        for i in range(6):
            # print(y[i])
            print(i)
            if y[i] == x[0]:
                aa.append(i)
        for i in range(len(aa)):
            a = aa[i]


            w = a+1
            if w>5:
                w-=6
            t = a-1
            if t>5:
                t-=6
            if y[w] == x[1]:
                direction = 1
            elif y[t] == x[1]:
                direction = -1
            else:
                # print(-1)
                # boo = False
                return False
            for j in range(6):
                # print(j, a+j*direction)
                ind = a+j*direction
                if ind>5:
                    # print(ind, 99)
                    ind -=6
                    # print(y[ind])
                if x[j] == y[ind]:
                    pass
                else:
                    # print(-1)
                    # boo = False
                    return False
    else:
        # boo = False
        return False

for i in range(n-1):
    if snowflake(snows[i], snows[i+1]) == False:
        print("No two snowflakes are alike.")
        sys.exit()

print("Twin snowflakes found.")
# import sys
# n = int(input())
# snows = []
# for i in range(n):
#     snows.append(list(map(int,input().split())))
# # print(snows)
#
# aa = []
# def snowflake(x, y):
#     boo = True
#     if x[0] in y:
#         for i in range(6):
#             # print(y[i])
#             if y[i] == x[0]:
#                 aa.append(i)
#         for i in range(len(aa)):
#             a = aa[i]
#
#
#             w = a+1
#             if w>5:
#                 w-=6
#             t = a-1
#             if t>5:
#                 t-=6
#             if y[w] == x[1]:
#                 direction = 1
#             elif y[t] == x[1]:
#                 direction = -1
#             else:
#                 # print(-1)
#                 # boo = False
#                 boo+=1
#                 return False
#             for j in range(6):
#                 # print(j, a+j*direction)
#                 ind = a+j*direction
#                 if ind>5:
#                     # print(ind, 99)
#                     ind -=6
#                     # print(y[ind])
#                 if x[j] == y[ind]:
#                     pass
#                 else:
#                     # print(-1)
#                     # boo = False
#                     boo += 1
#                     return False
#     else:
#         # boo = False
#         boo += 1
#         return False
#     if boo> n-2:
#         print("Twin snowflakes found.")
#         sys.exit()
#
# # for i in range(n-1):
# #     if boo> n-2:
# #         print("No two snowflakes are alike.")
# #         sys.exit()
# print("No two snowflakes are alike.")
#     # if snowflake(snows[i], snows[i+1]) == False:
#     #     print("No two snowflakes are alike.")
#     #     sys.exit()
#
#
#
# # if boo == True:
# #     print("Twin snowflakes found.")
# # else:
# #     print("No two snowflakes are alike.")