# import sys
# import heapq
# v = int(input())
# e = int(input())
# adj = {}
# inf = sys.maxsize
# nodedata = {}
# for i in range(1,v+1):
#     adj[i]= {}
#     nodedata[i] = {'cost':inf}
# for i in range(e):
#     s,d,c = map(int,input().split())
#     adj[s][d] = c
# queue=[]
# for i in range(int(input())):
#     a,b = map(int,input().split())
#     nodedata[a]['cost']=b
#     queue.append(a)
# d = int(input())
# global data
# data = []
# print(adj)
# print(nodedata)
# def dijkstra(src,dest):
#
#
#
#     data.append((nodedata[dest]['cost'],src))
#     print(nodedata[dest]['cost'])
# for i in queue:
#     print(i,d)
#     dijkstra(i,d)
import sys
import heapq


N = int(input())
M = int(input())


graph = {}
inf = sys.maxsize

for i in range(M):
    city1,city2,shipping = map(int,input().split())
    try:
        graph[city1].append((city2,shipping))
    except KeyError:
        graph[city1] = [(city2,shipping)]
    try:
        graph[city2].append((city1,shipping))
    except KeyError:
        graph[city2] = [(city1,shipping)]
K = int(input())
queries = {}
queries2 = []
for i in range(K):
    a,b = map(int,input().split())
    queries[a]=b
    # queries2.append((a,b))
D = int(input())
#
# dist = [inf for _ in range(N + 1)]
# dist[1] = 0
# queue = [(0,1)]
def dijkstra(node):
    dist = [inf for _ in range(N + 1)]
    dist[node] = queries[node]
    queue = [(dist[node], node)]
    while queue:
        # print(queue)
        # print(dist)
        # print(graph)
        distance, node = heapq.heappop(queue)
        if distance > dist[node]:
            continue
        for new_node,weight in graph.get(node,[]):
            new_dist = distance + weight
            if new_dist < dist[new_node]:
                dist[new_node] = new_dist
                heapq.heappush(queue,(dist[new_node],new_node))

    return(dist[D])

data = []
# print(queries)
for x in queries:
    heapq.heappush(data, dijkstra(x))

# print(data)
print(heapq.heappop(data))


