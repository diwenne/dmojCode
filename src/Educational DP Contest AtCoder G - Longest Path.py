import sys
sys.setrecursionlimit(100000)
v,e = map(int,input().split())
adj = [[]for _ in range(v+1)]
for i in range(1,e+1):
    a,b = map(int,input().split())
    adj[a].append(b)
nodedata=[0 for _ in range(v+1)]
def dp(node):
    # print(node,69)
    if nodedata[node]!= 0:
        return nodedata[node]
    maxlength = 0
    for i in adj[node]:
        maxlength = max(maxlength,dp(i))
    nodedata[node] = maxlength + 1
    # print(maxlength)
    return nodedata[node]
for i in range(1,v+1):
    dp(i)
print(max(nodedata)-1)

# def dp(src):
#     for i in range(v-1):
#         boo = False
#         for s in range(1,v+1):
#             for d in adj[s]:
#                 cost = nodedata[s] + 1
#                 if cost>nodedata[d]:
#                     nodedata[d]=cost
#                     boo=True
#         if boo == False:
#             # print(-1)
#             break
# dp(1)
# # for i in range(1,v+1):
# #     dp(i)
# print(max(nodedata))