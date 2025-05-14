for p in range(5):
    from collections import deque
    n,m = map(int,input().split())
    graph = []
    val = []
    for i in range(n):
        a = list(map(int,input().split()))
        graph.append(a)
        val.append(max(a))
    print(val)
    print(graph)
    counter = 0
    layers = {}

    directions = [(0,-1),(0,1),(-1,0),(1,0)]
    def bfs(height,x,y):
        queue = deque([(x,y)])
        counter2 = 0
        boo = True
        while queue:
            x,y = queue.popleft()
            # if (x,y) in prevvis:
            #     return 0
            if (x,y) not in vis:
                vis.add((x,y))
                print(x,y)
                counter2 += 1
                for i in directions:
                    newX = x+i[0]
                    newY = y+i[1]
                    if 0<=newX<n and 0<=newY<m and graph[newX][newY] < height:
                        print(newX,newY,-1)
                        queue.append((newX,newY))


                    else:
                        if not 0<=newX<n or not 0<=newY<m:
                            boo =False


        if boo ==False:
            return 0
        else:
            print(counter2,69)
            return counter2



    for i in range(1,max(val)+1):

        print(i,10000000)
        vis = set()
        for j in range(n):
            for k in range(m):
                if graph[j][k] < i:
                    counter += bfs(i,j,k)


    print(counter)

