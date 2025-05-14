# import sys
# n = int(input())
# nodedata=[[0,0,0] for _ in range(n+1)]
# values = [ _ for _ in range(n+1)]
#
# for i in range(1,n+1):
#     a,b,c = map(int,input().split())
#     if i == 1:
#         nodedata[i] = [a,b,c]
#     values[i]=[a,b,c]
# if n == 1:
#     print(max(values[1]))
#     sys.exit()
# print(nodedata)
# # print(values)
# def dp(nodedata):
#     for i in range(1,n):
#         print(nodedata[i])
#         for jj in range(3):
#             j = values[i][jj]
#             for kk in range(3):
#                 k = values[i+1][kk]
#                 print(i,j,k)
#                 print(jj,kk)
#                 if jj != kk:
#                     # print("yes")
#                     cost = nodedata[i][jj]+ values[i+1][kk]
#                     if cost>nodedata[i+1][kk]:
#                         # print(nodedata[i][jj],nodedata[i+1][kk])
#                         nodedata[i+1][kk] = cost
#                         print(nodedata[i+1])
#     print(max(nodedata[n]))
#
# dp(nodedata)
import sys; n = int(input());nodedata=[[0,0,0] for _ in range(n+1)];values = [ _ for _ in range(n+1)]
a = list(map(int,input().split()))
values[1]=a;nodedata[1] = a
for i in range(2,n+1):
    a,b,c = map(int,input().split())
    values[i]=[a,b,c]
# print(values)
for i in range(1,n):
    for jj in range(3):
        j = values[i][jj]
        for kk in range(3):
            k = values[i+1][kk]
            if jj != kk:
                cost = nodedata[i][jj]+ values[i+1][kk]
                if cost>nodedata[i+1][kk]:
                    nodedata[i+1][kk] = cost
print(max(nodedata[n]))