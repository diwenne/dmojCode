from collections import deque
v,e,t = map(int,input().split())
adj = {}
# for i in range(1,v+1):
#     adj[i] = []
for i in range(e):
    x,y = map(int,input().split())
    adj.setdefault(x,[]).append(y)

q = int(input())

# print(adj)


def bfs(node,length):
    queue = deque([(node,0)])
    vis = set()
    nodedata= [[] for _ in range(v+1)]
    for i in range(1,v+1):
        nodedata[i] = "Not enough hallways!"
    while queue:
        node, length = queue.popleft()
        # print(queue)
        if node not in vis:
            vis.add((node))
            nodedata[node] = length
            # print(node)
            # if node == end:
            #     # print(length*t)
            #     return length*t
            # else:
            if node in adj:
                for i in adj[node]:
                    queue.append((i,length+1))
    # nodedata[node]="Not enough hallways!"
    return nodedata
    # return "Not enough hallways!"
# print(bfs(1,0))
paths = [[] for _ in range(v+1)]
# print(paths)
for i in range(1,v+1):
    # print(i)
    paths[i] = bfs(i,0)
# print(paths)
for i in range(q):
    x,y = map(int,input().split())
    a = paths[x][y]
    if type(a)==str:
        print(a)
    elif type(a)==int:
        print(a*t)
# print(bfs(2,0))
# for i in range(q):
#     x,y = map(int,input().split())
#     try:
#         print(adj[x][y])
#     except IndexError:
#         print(bfs(x,0,y))
#         adj[x][y]=bfs(x,0,y)






# print(values)
