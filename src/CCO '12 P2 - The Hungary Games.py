import sys
import heapq
inf = sys.maxsize
n,m = map(int,input().split())
adj = [[]for _ in range(n+1)]
nodedata = [[inf,inf] for _ in range(n+1)]

for i in range(1,m+1):
    a,b,c = map(int,input().split())
    # print(a,b)
    adj[a].append((b,c))
# print(adj)
def dij(node):
    nodedata[node][0] = 0
    # nodedata[node][1] = inf
    queue = [(0,node)]
    while queue:
        # print(queue)
        distance,node = heapq.heappop(queue)
        # print(node)
        # print(distance,node)

        if distance > nodedata[node][0] and distance > nodedata[node][1]:
            # print(-111)
            #
            # if distance < nodedata[node][1]:
            #     nodedata[node][1] = dis
            # print(-1)
            continue

        for newnode,weight in adj[node]:

            # print(adj[node])
            newdist = distance+weight
            if newdist<nodedata[newnode][0]:
                # print(69)
                b = nodedata[newnode][0]
                if b<nodedata[newnode][1]:
                    nodedata[newnode][1] = b

                nodedata[newnode][0] = newdist

                # print(newnode,newdist, 1)
                heapq.heappush(queue,(newdist,newnode))
            elif newdist>nodedata[newnode][0] and newdist<nodedata[newnode][1]:
                nodedata[newnode][1] = newdist
                # print(newnode,newdist,-1)
                heapq.heappush(queue,(newdist,newnode))
    a = nodedata[n][1]
    if a == inf:
        print(-1)
    else:
        print(a)
dij(1)