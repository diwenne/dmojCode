t = int(input())
for i in range(t):
    from collections import deque
    r = int(input())
    c = int(input())
    arr = []
    end = (r-1,c-1)
    for i in range(r):
        arr.append(input())
    def bfs(x,y):
        queue = deque([[x, y, 1]])
        vis = set()

        while queue:
            x, y, length = queue.popleft()
            if (x, y) not in vis:
                # print(x,y)
                vis.add((x, y))
                a = arr[x][y]
                if a == "*":
                    directions = []
                elif a == "-":
                    directions = [[0, 1], [0, -1]]
                elif a == "|":
                    directions = [[1, 0],[-1, 0]]
                elif a == "+":
                    directions = [[1, 0],[-1, 0],[0, 1], [0, -1]]
                if (x,y) == end:
                    print(length)
                    return True

                else:
                    for i in directions:
                        newX = x + i[0]
                        newY = y + i[1]
                        if 0 <= newX < r and 0 <= newY < c:
                            if arr[newX][newY] != "*":
                                queue.append([newX, newY, length+1])

    if bfs(0,0) != True:
        print(-1)

