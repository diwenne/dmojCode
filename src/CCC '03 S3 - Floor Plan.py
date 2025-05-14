from collections import deque
m = int(input())
r = int(input())
c = int(input())
arr = []
v = []
directions = [[1,0],[0,1],[-1, 0],[0, -1]]
for i in range(r):
    arr.append(input())
# for i in arr:
#     print(i)
# queue = deque([(0,0)])
visited = set()
def bfs(row, col):
    queue = deque([(row, col)])
    counter = 0
    while queue:
            x, y = queue.popleft()
            if (x, y) not in visited:
                visited.add((x, y))
                a = arr[x][y]
                # print(a)
                if a == ".":
                    counter += 1
                for i in directions:
                    newX = x + i[0]
                    newY = y + i[1]
                    if 0 <= newX < r and 0 <= newY < c:
                        if arr[newX][newY] == ".":
                            queue.append((newX, newY))
                # print((x, y))
                # print(counter)
    if counter>0:
        v.append(counter)
for i in range(r):
    for j in range(c):
        if (r, c) not in visited and arr[i][j] != "I":
            bfs(i, j)
                # print(arr[r][c])
v.sort(reverse=True)
# print(v)
rooms = 0

for i in range(len(v)):
    if m- v[i] >=0:
        m-= v[i]
        rooms +=1
        if i == len(v)-1:
            if rooms == 1:
                print(str(rooms) + " room, " + str(m) + " square metre(s) left over")
                break
            else:
                print(str(rooms) + " rooms, " + str(m) + " square metre(s) left over")
                break
    else:
        if rooms == 1:
            print(str(rooms) + " room, " + str(m) + " square metre(s) left over")
            break
        else:
            print(str(rooms) + " rooms, " + str(m) + " square metre(s) left over")
            break
