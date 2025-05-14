from collections import deque
r = int(input())
c = int(input())
vis = set()
graph = []
values = 0
for i in range(r):
    graph.append(input())
# for i in graph:
    # print(i)
queue = deque([(int(input()), int(input()))])

directions = [(1,0), (-1, 0), (0, 1),(0, -1)]

while queue:
    # print(queue)
    x, y = queue.popleft()
    if (x,y) not in vis:
        vis.add((x,y))
        v = graph[x][y]
        if v == "S":
            values +=1
        if v == "M":
            values +=5
        if v == "L":
            values +=10

        for i in directions:
            newX = x + i[0]
            newY = y + i[1]
            if 0 <= newX < r and 0 <= newY < c:
                if graph[newX][newY] != "*":
                    queue.append((newX, newY))

print(values)


