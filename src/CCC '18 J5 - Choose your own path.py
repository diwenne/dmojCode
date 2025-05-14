pages = int(input())
adj = {}
for i in range(1, pages+1):
    inp = list(map(int,input().split()))
    # print(inp)
    adj[i] = inp[1:]

# print(adj)
def dfs(node, visited, adj):
    if node not in visited:
        visited.add(node)
        if len(visited) == pages:
            return True
        for i in adj[node]:
            if dfs(i, visited, adj):
                return True
if dfs(1, set(), adj):
    print("Y")
else:
    print("N")
def bfs(node):
    visited = [False] * (len(adj) + 1)
    queue = [[node,0]]
    visited[node] = True
    while queue:
        node, length = queue.pop(0)
        if len(adj[node]) == 0:
            return length
        else:
            for neighbour in adj[node]:
                if visited[neighbour] == False:
                    queue.append([neighbour,length+1])
                    visited[neighbour] = True
print(bfs(1)+1)
print(adj)


#
# for j in range(1, pages+1):
#     connections = int(input())
#     for h in range(m):
#         connection = int(input())
#         adj[j].append(connection)
# print(adj)

