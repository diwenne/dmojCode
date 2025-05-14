from collections import deque
n = int(input())
m = int(input())
adj=[[] for _ in range(m+1)]
for i in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
print(adj)
def bfs(node):
    queue= deque([node])
    vis = set()
    while queue:
        print(1)
        node = queue.popleft()
        if node not in vis:
            vis.add(node)
            for i in adj[node]:
                queue.append(i)
        elif node in vis and len(vis)!= n:
            print("N")
            return
    print("Y")
bfs(1)