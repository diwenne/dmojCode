#setup
from collections import deque
counter=0
w = input()
r = int(input())
c = int(input())

graph = []
directions = [(1,0), (-1, 0), (0, 1),(0, -1), (1,1), (1,-1), (-1,1),(-1,-1)]
#storing graph
for i in range(r):
    graph.append(input().replace(" ", ""))
for i in graph:
    print(i)

# def dfs(x,y)
#     visited = set()
#     if (x,y) not in visited:
#         visited.add((x,y))
#         if

def bfs(x,y):
    global counter2
    visited = set()
    queue = deque([[x,y,1, 0, w[0], False]])
    while queue:
        # print(queue)

        x,y,length,lastmove,word, boo = queue.popleft()
        # print(x, y, length, lastmove,word)
        # print(boo)

        # print(x,y, visited)
        # if (x,y) not in visited:
        #     visited.add((x,y))
            # print(-1)

        if word == w and len(queue)>0:
            counter2 +=1
            # print(71)
            for i in queue:
                # print(i)
                if i[4] == w:
                    counter2 += 1
                    # print(70)

            return
        elif word == w:
            counter2 += 1
            # print(69)
            return

        if boo == False and lastmove != 0:
            if lastmove in [(1,1), (-1,1), (1,-1),(-1,-1)]:
            # if lastmove == (1,-1):
            #     print(lastmove)
            #     print(-3)
                directionss = [(1,1),(-1,1),(1,-1),(-1,-1)]
            elif lastmove in [(1,0),(-1,0),(0,1),(0,-1)]:
                # print(lastmove)
                # print(-2)
                directionss = [(1,0),(-1,0),(0,1),(0,-1)]
            for i in directionss:
                # print(10)
                # print(i)
                newX = x + i[0]
                newY = y + i[1]
                if 0 <= newX < r and 0 <= newY < c:
                    if graph[newX][newY] == w[length] and i != lastmove :
                        # print(newX, newY), print(lastmove)
                        queue.append([newX, newY, length + 1, i, word + graph[newX][newY], True])
                    elif graph[newX][newY] == w[length] and i == lastmove:
                        queue.append([newX, newY, length + 1, i, word + graph[newX][newY], False])


        elif lastmove != 0:
            newX = x+lastmove[0]
            newY = y+lastmove[1]
            # print(lastmove)
            if 0 <= newX < r and 0 <= newY < c:
                # print(-1)
                if graph[newX][newY] == w[length]:
                    queue.append([newX, newY, length+1, lastmove, word+w[length], True])


                    # print(42)


        else:
            if lastmove == 0:
                for i in directions:
                    # print(i)
                    newX = x+i[0]
                    newY = y+i[1]
                    if 0 <= newX<r and 0 <= newY<c:
                        if graph[newX][newY] == w[length]:
                            # print(w[length])
                            # print(newX,newY)
                            # print(graph[newX][newY])
                            queue.append([newX, newY, length+1, i, word+w[length], False])
                            # print(69)


for i in range(r):
    for j in range(c):
        counter2 = 0
        if graph[i][j] == w[0]:
            bfs(i, j)
                # print("yes")
            counter+=counter2
            # else:
                # print("no")
            # print(w)

print(counter)


