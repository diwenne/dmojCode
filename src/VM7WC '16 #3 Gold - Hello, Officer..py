import heapq
import sys
n,m,b,q = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))
    graph[y].append((x,z))



inf = sys.maxsize


dist = [inf for _ in range(n + 1)]
def dijkstra(src):
    queue = [(0, src)]
    dist[src] = 0
    while queue:
        distance, node = heapq.heappop(queue)
        if distance > dist[node]:
            continue
        # print(distance,node)
        for new_node, weight in graph[node]:
            new_dist = distance + weight
            if new_dist < dist[new_node]:
                dist[new_node] = new_dist
                heapq.heappush(queue, (dist[new_node], new_node))
    for i in range(n+1):
        if dist[i] == inf:
            dist[i] = -1
dijkstra(b)
for i in range(q):
    a = int(input())

    print(dist[a])
#         # print(dist)
# print(dist)
#
# print(b)