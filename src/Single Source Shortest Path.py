
# # import sys
# # from heapq import heapify, heappop, heappush
# # inf = sys.maxsize
# # v, e = map(int,input().split())
# # adj = {}
# # for i in range(1,v+1):
# #     adj[str(i)]={}
# # for i in range(e):
# #     s,d,w = map(int,input().split())
# #     adj[str(s)][str(d)]=w
# # # print(adj)
# #
# # nodedata={}
# # for i in range(1, v+1):
# #     nodedata[str(i)] = {"cost":inf, "pred":[]}
# # # print(nodedata)
# #
# # def belleman(graph,src,dest):
# #     nodedata[src]['cost']=0
# #     for i in range(v-1):
# #         for itr in graph:
# #             for neighbour in graph[itr]:
# #                 cost = nodedata[itr]['cost']+graph[itr][neighbour]
# #                 if cost<nodedata[neighbour]['cost']:
# #                     nodedata[neighbour]['cost'] = cost
# #         # print(nodedata)
# #     for i in range(1, v + 1):
# #         if nodedata[str(i)]['cost'] == inf:
# #             nodedata[str(i)]['cost'] = -1
# #     print(nodedata[dest]['cost'])
# # for i in range(1,v+1):
# #     belleman(adj,'1',str(i))
# import sys
#
# inf = sys.maxsize
# global v
# v, e = map(int, input().split())
#
# adj = {}
# for i in range(1, v + 1):
#     adj[str(i)] = {}
#
# for i in range(e):
#     s, d, w = map(int, input().split())
#     adj[str(s)][str(d)] = w
#     adj[str(d)][str(s)] = w
#
# nodedata = {}
# for i in range(1, v + 1):
#     nodedata[str(i)] = {"cost": inf, "pred": []}
#
# def bellman(graph, src, dest,v):
#     nodedata[src]['cost'] = 0
#     for _ in range(v - 1):
#         for u in graph:
#             for v in graph[u]:
#                 if nodedata[u]['cost'] + graph[u][v] < nodedata[v]['cost']:
#                     nodedata[v]['cost'] = nodedata[u]['cost'] + graph[u][v]
#     if nodedata[str(i)]['cost'] == inf:
#         nodedata[str(i)]['cost'] = -1
#
# bellman(adj, '1', str(v),v)
# for i in range(1, v + 1):
#     print(nodedata[str(i)]['cost'])
from collections import deque
import heapq
import sys
n,w = map(int,input().split())
graph = {}
for i in range(w):
    a,b,c = map(int,input().split())
    graph.setdefault(a,[]).append((b,c))
    graph.setdefault(b,[]).append((a,c))
inf=sys.maxsize
dist = [inf for _ in range(n + 1)]
def dijkstra(src):
    queue = [(0,src)]
    dist[src]=0
    while queue:
        # print(queue)
        distance, node = heapq.heappop(queue)
        if distance > dist[node]:
            continue
        # print(graph)
        for new_node, weight in graph.get(node, []):
            new_dist = distance + weight
            if new_dist < dist[new_node]:
                dist[new_node] = new_dist
                heapq.heappush(queue, (dist[new_node], new_node))
    # print(dist)
    for i in range(len(dist)):
        if dist[i] == inf:
            dist[i] = -1

dijkstra(1)
for i in range(1, n + 1):
    print(dist[i])