import sys

inf = sys.maxsize

v, e = map(int, input().split())

adj = {}
for i in range(1, v + 1):
    adj[str(i)] = {}

for i in range(e):
    s, d, w = map(int, input().split())
    adj[str(s)][str(d)] = w

nodedata = {}
for i in range(1, v + 1):
    nodedata[str(i)] = {"cost": inf, "pred": []}

def bellman(graph, src, dest,v):
    nodedata[src]['cost'] = 0
    for _ in range(v - 1):
        for u in graph:
            for v in graph[u]:
                if nodedata[u]['cost'] + graph[u][v] < nodedata[v]['cost']:
                    nodedata[v]['cost'] = nodedata[u]['cost'] + graph[u][v]
    print(nodedata[dest]['cost'])

bellman(adj, '1', str(v),v)
# import sys
# import copy
# # from heapq import heapify, heappop, heappush
# inf = sys.maxsize
# v, e = map(int,input().split())
# adj = {}
# for i in range(1,v+1):
#     adj[str(i)]={}
# for i in range(e):
#     s,d,w = map(int,input().split())
#     adj[str(s)][str(d)]=w
# # print(adj)
#
# nodedata={}
# for i in range(1, v+1):
#     nodedata[str(i)] = {"cost":inf, "pred":[]}
# # print(nodedata)
#
# def belleman(graph,src,dest):
#     nodedata[src]['cost']=0
#     for i in range(v-1):
#         nodedata2 = copy.deepcopy(nodedata)
#         for itr in graph:
#             for neighbour in graph[itr]:
#                 cost = nodedata[itr]['cost']+graph[itr][neighbour]
#                 if cost<nodedata[neighbour]['cost']:
#                     nodedata[neighbour]['cost'] = cost
#         if nodedata == nodedata2:
#             break
#
#         # print(nodedata)
#     print(nodedata[dest]['cost'])
# belleman(adj,'1',str(v))


# def dijkstra(graph, src, dest):
#     nodedata[src]['cost']=0
#     visited = []
#     temp = src
#     for i in range(v-1):
#         if temp not in visited:
#             visited.append(temp)
#             min_heap = []
#             for j in adj[temp]:
#                 if j not in visited:
#                     cost = nodedata[temp]['cost']+adj[temp][j]
#                     if cost < nodedata[j]['cost']:
#                         nodedata[j]['cost'] = cost
#                         nodedata[j]['pred'] = nodedata[j]['pred'] + list(temp)
#                     heappush(min_heap,(nodedata[j]['cost'], j))
#         heapify(min_heap)
#         a
x
#     # print(nodedata)
#     # for i in range(1,v+1):
#     #     if nodedata[str(i)]['cost']==inf:
#     #         nodedata[str(i)]['cost'] = -1
#     print(nodedata[dest]['cost'])
# dijkstra(adj,'1',str(v)) m



