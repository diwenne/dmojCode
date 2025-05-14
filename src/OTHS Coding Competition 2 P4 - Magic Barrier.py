n,m,q = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

def check(k,r1,c1,r2,c2):
    for row in range(r1,r2+1):
        for col in range(c1,c2+1):
            # print(row,col)
            # print(graph[row-1][col-1])
            if graph[row-1][col-1] == k:
                return True
    return False
for i in range(q):
    k,r1,c1,r2,c2 = map(int,input().split())
    print(check(k,r1,c1,r2,c2))