import sys
import heap
k,n,m = map(int,input().split())
adj = [[]for _ in range(n+1)]
inf = sys.maxsize
nodedata = [{} for _ in range(n+1)]
for i in range(m):
    a,b,t,h = map(int,input().split())
    adj[a].append((b,t,h))
    adj[b].append((a,t,h))
def dijkstra(src,dest):
    nodedata[src] = 0
    queue= [(0,src,0)]
    while queue:
        distance,node,dmg = heapq.heappop(queue)
        if distance > nodedata[node]:
            continue
        elif dmg >k:
            continue
        for newnode,weight,newnodedmg in adj[node]:
            newdist = distance + weight
            for dmgs in nodedata[node].get(dmgs, inf)
            if newdist < nodedata[newnode]:
                nodedata[newnode] = newdist

print(adj)
