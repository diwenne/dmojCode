n = int(input())
graph = {}
for i in range(1, n+1):
    graph[i]=[]

for i in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)

x, y = map(int, input().split())

def dfs(node,visited, graph):
    if node not in visited:
        visited.add(node)
        if node == y:
            return True

        for neighbour in graph[node]:
             if dfs(neighbour,visited,graph):
                 return True

if dfs(x,set(),graph):
    print("Tangled")
else:
    print("Not Tangled")