import sys
from collections import deque
n,m,q,c = map(int,input().split())
adj = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
inf = sys.maxsize
nodedata = [inf for _ in range(n+1)]
def bfs(node):
    queue=deque([(node,0)])
    # print(queue)
    vis = set()
    while queue:
        node,length = queue.popleft()
        if node not in vis:
            vis.add(node)

            nodedata[node] = length

            for i in adj[node]:
                queue.append((i,length+1))
    for i in range(n+1):
        if nodedata[i] == inf:
            nodedata[i] = "NA"


bfs(c)
for i in range(q):
    a,b = map(int,input().split())
    try:
        x = int(nodedata[a])
        y = int(nodedata[b])
        print(x+y)
    except:
        print("This is a scam!")
# print(adj)
# print(nodedata)

# print(adj)