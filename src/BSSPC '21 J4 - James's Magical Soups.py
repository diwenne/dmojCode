import heapq
x,n = map(int,input().split())
soups = []
for i in range(n):
    a,b = map(int,input().split())
    soups.append((a,b))
counter = 0
queue = []
ind = 0
vis = set()
while len(vis)<n:
    # print(ind,"minute")
    temp = x+ind
    # print(temp,"maxtemp")
    # print(soups)
    for t,f in soups:
        if (t,f) not in vis:
            # print(t,f)
            if t<=temp:
                heapq.heappush(queue,(f,t))
                vis.add((t,f))

    # print(queue)
    while queue:
        expiry, t = heapq.heappop(queue)
        if expiry >=ind:
            # print(expiry,100)
            counter +=1
            break


    ind+=1
# print(queue)
while queue:
    expiry, t = heapq.heappop(queue)
    if expiry >=ind:
        # print(expiry,100)
        counter +=1
print(counter)