n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
type=0
if graph[0][0]>graph[0][1]:
    if graph[0][0]>graph[1][0]:
        type=180
    else:
        type =270
elif graph[0][0]>graph[1][0]:
    if graph[0][0] > graph[0][1]:
        type = 180
    else:
        type=90
else:
    type=360

newgraph=[[]for _ in range(n)]
if type==90:
    for i in range(n):
        for j in range(n):
            newgraph[i].append(graph[n-j-1][i])

elif type == 180:
    for i in range(n):
        for j in range(n):
            newgraph[i].append(graph[n-i-1][n-j-1])

elif type == 270:
    # print(1)
    for i in range(n):
        for j in range(n):
            newgraph[i].append(graph[j][n-i-1])

elif type == 360:
    newgraph= graph


for i in newgraph:
    print(*i)

