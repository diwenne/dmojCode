import sys
from collections import deque
# righttop = [(0,1), (0,2), (0,3), (0,4),(0,4) ,(1,4) ,(2,4), (3,4) ]
# leftbot = [(0,1), (0,2), (0,3), (0,4),(0,4) ,(1,4) ,(2,4), (3,4) ]
r,c,k = map(int,input().split())

obstacles = set()
for i in range(k):
    # a,b = map(int,input().split())
    obstacles.add((map(int,input().split())))
directions = [(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
# for i in arr:
#     print(i)
leftbot = set()  #finding with nodes are along the left and bottom edges
for i in range(1,c-1):
    if (r,i+1) in obstacles:
        leftbot.add((r,i+1))
for i in range(1,r):
    if (i+1,1) in obstacles:
        leftbot.add((i+1,1))

# print(leftbot)
righttop = set()   #vice versa
for i in range(1,c-1):
    if (1,i+1) in obstacles:
        righttop.add((1,i+1))

if (1,c) in obstacles:
    righttop.add((1,c))
for i in range(1,r):
    if (i+1,c) in obstacles:
        righttop.add((i+1,c))

# print(righttop)
def bfs(x,y):
    queue = deque([(x,y)])
    while queue:
        # print(queue)
        x,y = queue.popleft()
        if (x,y) not in vis:
            vis.add((x,y))
            if (x,y) in righttop:   #if a node from the bottom/left, can travel to right/top, means the wayis blocked
                # print(x,y)
                # print(69)
                return True
            else:
                for i in directions:
                    newX = x + i[0]
                    newY = y + i[1]
                    if 1 <= newX < r+1 and 1 <= newY < c+1:
                        if (newX,newY) in obstacles:
                            queue.append((newX,newY))
# # print(arr)
# print(righttop)
# print(leftbot)
# print(obstacles)
vis = set()
for i in leftbot:
    if bfs(i[0],i[1]):
        print("NO")
        sys.exit()

print("YES")

# import sys
# from collections import deque
# # righttop = [(0,1), (0,2), (0,3), (0,4),(0,4) ,(1,4) ,(2,4), (3,4) ]
# # leftbot = [(0,1), (0,2), (0,3), (0,4),(0,4) ,(1,4) ,(2,4), (3,4) ]
# r,c,k = map(int,input().split())
# arr = []
# for i in range(r):
#     arr.append(["." for _ in range(c)])
# for i in range(k):
#     a,b = map(int,input().split())
#     arr[a-1][b-1] = "#"
# directions = [(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
# # for i in arr:
# #     print(i)
# leftbot = set()
# for i in range(1,c-1):
#     if arr[r-1][i] == "#":
#         leftbot.add((r-1,i))
# for i in range(1,r):
#     if arr[i][0] == "#":
#         leftbot.add((i,0))
#
# # print(leftbot)
# righttop = set()
# for i in range(1,c-1):
#     if arr[0][i] == "#":
#         righttop.add((0,i))
# righttop.remove((0,0))
# righttop.add((0,c-1))
# for i in range(1,r):
#     if arr[i][c-1] == "#":
#         righttop.add((i,c-1))
#
# # print(righttop)
# def bfs(x,y):
#     queue = deque([(x,y)])
#     vis = set()
#     while queue:
#         # print(queue)
#         x,y = queue.popleft()
#         if (x,y) not in vis:
#             vis.add((x,y))
#             if (x,y) in righttop:
#                 # print(x,y)
#                 # print(69)
#                 return True
#             else:
#                 for i in directions:
#                     newX = x + i[0]
#                     newY = y + i[1]
#                     if 0 <= newX < r and 0 <= newY < c:
#                         if arr[newX][newY] != ".":
#                             queue.append((newX,newY))
#
# for i in leftbot:
#     if bfs(i[0],i[1]):
#         print("NO")
#         sys.exit()
#
# print("YES")

