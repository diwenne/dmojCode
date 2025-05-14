# n, m, x, y = map(int, input().split())
# p = []
# graph = {}
# for i in range(1, n+1):
#     graph[i]=[]
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# def dfs(node,visited, graph):
#     if node not in visited:
#         visited.add(node)
#         # do whatever
#         # print(node)
#         if y in visited:
#             print("GO SHAHIR!")
#             p.append(1)
#             return
#         # print(visited)
#         for neighbour in graph[node]:
#             dfs(neighbour,visited,graph)
# dfs(x,set(),graph)
#
# while not p:
#     print("NO SHAHIR!")
#     break
# print(graph)
n, m, x, y = map(int, input().split())
graph = {}
for i in range(1, n+1):
    graph[i]=[]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node,visited, graph):
    if node not in visited:
        visited.add(node)
        if node == y:
            return True
        for neighbour in graph[node]:
             if dfs(neighbour,visited,graph):
                 return True

if dfs(x,set(),graph):
    print("GO SHAHIR!")
else:
    print("NO SHAHIR!")

