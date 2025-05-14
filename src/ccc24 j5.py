from collections import deque
r,c = int(input()),int(input())
directions = [[1,0],[0,1],[-1,0],[0,-1]]
grid = []
v = 0

for i in range(r):
    grid.append(input())
vis = set()
queue = deque([[int(input()),int(input())]])
for i in grid:
    print(i)

while queue:
    # print(queue)
    print(queue)
    x,y = queue.popleft()
    print(x, y)
    if (x,y) not in vis:
        vis.add((x,y))
        a = grid[x][y]

        if a == "L":
            v += 10
        elif a == "M":
            v += 5
        else:
            v += 1

        for i in directions:
            newX = x + i[0]
            newY = y + i[1]
            if 0 <= newX < r and 0 <= newY < c and grid[newX][newY] != "*":
                queue.append([newX,newY])

print(v)
print(grid)



# row = int(input())
# col = int(input())
# arr = []
#
# for i in range(row):
#     rowdetails = input()
#     lis = []
#     for i in rowdetails:
#         lis.append(i)
#     arr.append(lis)
# rowstart = int(input())
# colstart = int(input())
# #calculating
# boole= False
# print(row-(row-rowstart)-1)
# for i in range(row-(row-rowstart)-1):
#
#     rowstart -=1
#     if arr[rowstart][colstart] == "*":
#         print(rowstart)
#         boole = True
#         break
# if boole == False:
#     print(rowstart)
#
#
# # total = 0
# # for i in arr:
# #     for j in i:
# #         if j == "L":
# #             total += 10
# #         if j == "M":
# #             total += 5
# #         if j == "S":
# #             total += 1
# # print(total)
# harvested = 0
# values = {"L": 10,"M": 5,"S": 1}
# def dfs(x, y, visited):
#     adj = [[0,1],[1,0],[0,-1],[-1,0]]
#     if (x,y) not in visited:
#         visited.add((x, y))
#         if arr[x][y] == None or "*":
#             return
#         if not arr[x][y] == "*":
#             harvested+= values[adj[x][y]]
#         for i in adj:
#             newX = i[0] + x
#             newY = i[1] + y
#
#             if 0 <= newX < row and 0 <= newY < col:
#                 dfs(newX,newY,visited)
#
# dfs(rowstart, colstart, set())
# print(harvested)





# for i in arr:
#     print(i)
