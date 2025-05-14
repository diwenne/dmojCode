adj = {
    1:{6},
    2:{6},
    3:{4, 6, 5, 15},
    4:{6, 3, 5},
    5:{6, 4, 3},
    6:{1, 2, 7, 5, 4, 3},
    7:{6, 8},
    8:{7, 9},
    9:{8, 12, 10},
    10:{9, 11},
    11:{10, 12},
    12:{9, 11, 13},
    13:{12, 15, 14},
    14:{13},
    15:{3, 13},
    16:{18, 17},
    17:{16, 18},
    18:{16, 17},
}
# print(adj)
while True:
    cmd = input()
    if cmd == "i":
        x = int(input())
        y = int(input())

        adj.setdefault(x, set()).add(y)
        adj.setdefault(x, set()).add(y)

    elif cmd == "d":
        x = int(input())
        y = int(input())
        if not y in adj[x]:
            pass
        else:
            adj[x].remove(y)
            adj[y].remove(x)
    elif cmd == "n":
        x = int(input())
        print(len(adj[x]))
    elif cmd == "f":
        x = int(input())
        counter = set()
        for neighbour in adj[x]:
            for i in adj[neighbour]:
                counter.add(i)
            # print(counter)
            if x in adj[neighbour]:
                counter.remove(x)
            for i in adj[x]:
                if i in adj[neighbour]:
                    counter.remove(i)
        print(len(counter))

    elif cmd == "s":
        x = int(input())
        y = int(input())
        def bfs(node):
            visited = set()
            queue = [[node, 0]]
            visited.add(node)
            while queue:
                node, length = queue.pop(0)
                if node == y:
                    return length
                else:
                    for neighbour in adj[node]:
                        if neighbour not in visited:
                            queue.append([neighbour, length + 1])
                            visited.add(neighbour)
        if bfs(x)== None:
            print("Not connected")
        else:
            print(bfs(x))

    elif cmd == "q":
        break
