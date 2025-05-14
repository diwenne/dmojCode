# n, m = map(int, input().split())
# adjr = {}
# adjl = {}
# for i in range(1, n+1):
#     adjr[i] = []
#     adjl[i] = []
#
# for i in range(m):
#     x, y = map(int, input().split())
#     adjr[x].append(y)
#     adjl[y].append(x)
# start, end = map(int, input().split())
#
# # def dfs(node, visited, adj):
# #     if node not in visited:
# #         visited.add(node)
# #         if node == end:
# #             return True
# #         for neighbour in adj[node]:
# #             if dfs(neighbour, visited, adj):
# #                 return True
# def bfs(node, adj):
#     visited = [False] * (len(adj) + 1)
#     queue = [[node,0]]
#     visited[node] = True
#     while queue:
#         node, length = queue.pop(0)
#         if node == end:
#             return True
#         else:
#             for neighbour in adj[node]:
#                 if visited[neighbour] == False:
#                     queue.append([neighbour,length+1])
#                     visited[neighbour] = True
# if bfs(start, adjr):
#     print("yes")
# else:
#     if bfs(start, adjl):
#         print("no")
#     else:
#         print("unknown")
# print(adjr, adjl)
import sys
n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    adj[x].append(y)
start, end = map(int, input().split())

def dfs(node, visited, adj, end):
    if node not in visited:
        visited.add(node)
        if node == end:
            return True
        for neighbour in adj[node]:
            if dfs(neighbour, visited, adj, end):
                return True

if dfs(start, set(), adj, end):
    print("yes")
else:
    if dfs(end,set(), adj, start):
        print("no")
    else:
        print("unknown")