import heapq
import sys
n,m = map(int,input().split())
adj = [[]for _ in range(n)]
for i in range(m):
    x,y,t = map(int,input().split())
    adj[x].append((y,t))
    adj[y].append((x,t))
inf = sys.maxsize
nodedata0 = [inf for _ in range(n)]
nodedataN = [inf for _ in range(n)]
def dijkstra(node,dist_arr):
    dist_arr[node] = 0
    queue = [(0,node)]
    while queue:
        distance,node = heapq.heappop(queue)
        if distance> dist_arr[node]:
            continue
        for new_node,time in adj[node]:
            # print(time,new_node)
            cost = distance + time
            if cost < dist_arr[new_node]:
                dist_arr[new_node] = cost
                heapq.heappush(queue, (cost,new_node))
    # print(dist_arr)
# print(adj)
dijkstra(0,nodedata0)
# print(n)
dijkstra(n-1,nodedataN)
maxtime = 0
for i in range(n):
    total_time = nodedata0[i] + nodedataN[i]
    maxtime = max(maxtime, total_time)
print(maxtime)