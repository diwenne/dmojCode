import sys
inf = sys.maxsize
n = int(input())
adj = [[] for _ in range(n+1)]
nodedata = [inf for _ in range(n+1)]
for i in range(1,n+1):
    a = i+1
    b = i+2
    # print(a,b)
    if a<=n:
        adj[i].append(a)
    if b<=n:
        adj[i].append(b)
heights = list(map(int, input().split()))
heights.insert(0,0)
# print(adj)

def dp(src,dest):
    nodedata[src] = 0
    for i in range(n-1):
        boo = False
        for u in range(1,len(adj)):
            # print(u)
            for v in adj[u]:
                cost = abs(heights[u]-heights[v])
                if nodedata[u]!=inf:
                    cost+= nodedata[u]
                # print(cost)
                if cost < nodedata[v]:
                    boo = True
                    nodedata[v]=cost
            if boo == False:
                break
            # print(nodedata)
    print(nodedata[dest])

dp(1,n)