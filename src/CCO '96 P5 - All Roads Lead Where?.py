m,q = map(int,input().split())
graph = {}
for i in range(m):
    city1,city2 = input().split()
    graph.setdefault(city1,[]).append(city2)
    graph.setdefault(city2, []).append(city1)
def dfs(vis,node,dest,pred):
    if node not in vis:
        vis.add(node)
        # print(vis,node,dest,length)
        if node == dest:

            print(pred)
            return True

        for i in graph[node]:
            # print(i,length)
            if dfs(vis,i,dest,pred+i[0]):
                return True
for query in range(q):
    src,dest = input().split()
    dfs(set(), src, dest,src[0] )


# print(graph)