from collections import deque
    graph = []
    unions = set()
    n,m = map(int,input().split())
    parent = [ i for i in range(n+1)]
    # print(parent)
    def find(a):
        if a == parent[a]:
            return a
        else:
            return find(parent[a])
    def union(a,b):
        # print(find(a),find(b))

        parent[find(b)]= find(a)
    for i in range(m):
        lis = list(map(int,input().split()))
        lis.pop(0)

        graph.append(sorted(lis))

    i = graph[0]
    # print(i)
    for j in range(0,len(i)-1):

        union(i[j],i[j+1])


    for i in graph[0]:
        unions.add(i)
    for i in graph:
        if i == graph[0]:
            continue

        for j in i:
            if j in unions:
                for h in i:
                    union(j,h)
                    unions.add(h)
                continue


    parent = parent[1:]
    if 1 in unions:
        print(len(unions))
        for i in range(1,n+1):
            if i in unions:
                print(i,end=" ")
        print("")
    else:
        print(1)
        print(1)
# print(parent)
# print(unions)
'''
Union (1,2,3)
add the parent of all these unions to a set called unions
go through second set [2,3,4,5]
check if the parent of any of them is in unions if so then make the parent of this set that parent
otherwise, union these and add this parent to unions
'''

# union 2 parent is now 1
# 3s parent is now 1

