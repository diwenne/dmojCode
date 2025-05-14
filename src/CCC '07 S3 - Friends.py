from collections import deque

n = int(input())
adj = {}
for i in range(n):
    a,b = input().split()
    adj[a]=b

def bfs(x,y):
    print(-10)
    y = str(y)
    queue = deque([(x,-1)])
    vis = set()
    while queue:
        # print(queue)
        x,length = queue.popleft()
        x = str(x)
        if x not in vis:
            vis.add(x)

            if x == y:
                # print(1)
                print("Yes",length)
                return

            else:
                queue.append((adj[x],length+1))
    print("No")
    return
# print(adj["5000"])
while True:
    a,b = input().split()
    print(a,b)
    # print(a,b)
    if (a,b) == ("0","0"):
        break
    else:
        # print(a,b)
        bfs(a,b)

# 6
# 1 2
# 2 3
# 3 1
# 10 11
# 100 10
# 11 100
# 1 100
# 2 3
# 0 0

# print(adj)
