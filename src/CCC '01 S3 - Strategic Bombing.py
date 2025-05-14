adj = {}
roads = []
bombed = []
start = "A"




while True:
    road = input()
    if road == "**":
        break
    roads.append(road)

for j in range(len(roads)):
    x = roads[j][0]
    y = roads[j][1]
    adj.setdefault(x,[]).append(y)
    adj.setdefault(y, []).append(x)

# print(adj)
# print(roads)
for i in range(len(roads)):

    if i > 0:
        adj[removed[0]].append(removed[1])
        adj[removed[1]].append(removed[0])
    removed = roads[i]
    adj[removed[0]].remove(removed[1])
    adj[removed[1]].remove(removed[0])

    def dfs(node, visited, graph):
        if node not in visited:
            visited.add(node)
            if node == "B":
                return True
            for neighbour in graph[node]:
                if dfs(neighbour, visited, graph):
                    return True
    if not dfs("A", set(), adj):
        bombed.append(removed)


    # print(adj)
if len(bombed) == 0:
    print("There are 0 disconnecting roads.")
else:
    for i in range(len(bombed)):
        print(bombed[i])
    print("There are", str(len(bombed)),"disconnecting roads." )




# print(bombed)

# graph = {
#         "A": [],
#         "B": [],
#         "C": [],
#         "D": [],
#         "E": [],
#         "F": [],
#         "G": [],
#         "H": [],
#         "I": [],
#         "J": [],
#         "K": [],
#         "L": [],
#         "M": [],
#         "N": [],
#         "O": [],
#         "P": [],
#         "Q": [],
#         "R": [],
#         "S": [],
#         "T": [],
#         "U": [],
#         "V": [],
#         "W": [],
#         "X": [],
#         "Y": [],
#         "Z": [],
#         }

# roads = []
# bombed = []
# start = "A"
#
# while True:
#     road = input()
#     if road == "**":
#         break
#     roads.append(road)
#
# print(roads)
# for i in range(len(roads)):
#     adj = {}
#     p = False
#     for j in range(len(roads)):
#         x = roads[j][0]
#         y = roads[j][1]
#         adj.setdefault(x,[]).append(y)
#         adj.setdefault(y, []).append(x)
#     toberemoved = roads[0]
#     print(adj)
#
#
    # def dfs(node, visited, graph):
    #     if node not in visited:
    #         visited.add(node)
    #         # print(node)
    #         if node == "B":
    #             p = True
    #             return
    #         for neighbour in graph[node]:
    #             dfs(neighbour, visited, graph)
#
#     if start in adj:
#         dfs(start, set(), adj)
#     else:
#         start = roads[0][1]
#         dfs(start, set(), adj)
#
#     if p == True:
#         bombed.append(toberemoved)
#     roads.pop(0)
#
#
# print(bombed)
# print(roads)
# print(adj)
# while True:
#     road = input()
#     x = road[0]
#     y = road[1]
#     if road == "**":
#         break
#     roads.append(road)
#     adj.setdefault(x,[]).append(y)
#     adj.setdefault(y,[]).append(x)
# for i in range(len(roads)):
#     adj[roads[i][0]].remove(roads[i][0])
#     adj[roads[i][0]].remove(roads[i][1])
#     print(adj[roads[i][0]])
# print(roads)




#
# def dfs(node, visited, graph):
#     if node not in visited:
#         visited.add(node)
#         print(node)
#         if node == "B":
#             print(visited)
#             return
#         for neighbour in graph[node]:
#             dfs(neighbour, visited, graph)
#
# dfs("A", set(), adj)
# print(adj)