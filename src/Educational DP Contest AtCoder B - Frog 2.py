# import sys
# inf = sys.maxsize
# n,k = map(int,input().split())
# adj = [[] for _ in range(n+1)]
# nodedata = [inf for _ in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         if i+j<=n:
#             adj[i].append(i+j)
#
# # print(adj)
# heights = list(map(int, input().split()))
# heights.insert(0,0)
# # print(adj)
#
# def dp(src,dest):
#     nodedata[src] = 0
#     for i in range(n-1):
#         boo = False
#         for u in range(1,len(adj)):
#             # print(u)
#             for v in adj[u]:
#                 cost = abs(heights[u]-heights[v])
#                 if nodedata[u]!=inf:
#                     cost+= nodedata[u]
#                 # print(cost)
#                 if cost < nodedata[v]:
#                     boo = True
#                     nodedata[v]=cost
#             if boo == False:
#                 break
#             # print(nodedata)
#     print(nodedata[dest])
#
# dp(1,n)


n = int(input())
l = list(map(int,input().split()))
dp = [float('inf') for _ in range(n)]
dp[0] = 0
dp[1] = abs(l[0] - l[1])

for i in range(n-2):

    if dp[i] + abs(l[i] - l[i+2]) < dp[i+1] + abs(l[i+1]- l[i+2]):
        dp[i+2] = dp[i] + abs(l[i] - l[i+2])
        print(dp[i] + abs(l[i] - l[i+2]))
    else:
        dp[i+2] = dp[i+1] + abs(l[i+1] - l[i+2])
print(dp)
print(dp[-1])