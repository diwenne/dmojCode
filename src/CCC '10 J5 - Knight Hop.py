from collections import deque
s1, s2 = map(int, input().split())
e1, e2 = map(int, input().split())
lis = [s1, s2, e1, e2]
for i in range(len(lis)):
    lis[i] = 8 - lis[i]
s1 = lis[0]
s2 = lis[1]
e1 = lis[2]
e2 = lis[3]
directions = [[1, 2],[-1, 2],[1, -2],[-1, -2],[2, 1],[-2, 1],[2, -1],[-2, -1]]
def bfs(x,y):
    visited = set()
    visited.add((x,y))
    queue = deque([[x,y, 0]])
    while True:
        # print(x,y)
        x, y, length = queue.popleft()
        if (x,y) == (e1, e2):
            return length
        else:
            for i in directions:
                newX = x + i[0]
                newY = y + i[1]
                if 0<= newX < 8 and 0<= newY <8:
                    # print(i)
                    # print(x, y)
                    queue.append([newX, newY, length+1])
print(bfs(s1, s2))




