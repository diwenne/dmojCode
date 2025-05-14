from collections import deque
import heapq
import sys
n,w,p = map(int,input().split())
graph = {}
for i in range(w):
    a,b,c = map(int,input().split())
    graph.setdefault(a,[]).append((b,c))
    graph.setdefault(b,[]).append((a,c))
inf=sys.maxsize

def dijkstra(src,dest):
    dist = [inf for _ in range(n + 1)]
    queue = [(0,src)]
    dist[src]=0
    while queue:
        distance, node = heapq.heappop(queue)
        if distance > dist[node]:
            continue
        for new_node, weight in graph.get(node, []):
            new_dist = distance + weight
            if new_dist < dist[new_node]:
                dist[new_node] = new_dist
                heapq.heappush(queue, (dist[new_node], new_node))
    # print(dist)
    print(dist[dest])
for i in range(p):
    a,b = map(int,input().split())
    dijkstra(a,b)
# print(graph)
