import heapq
g = int(input())
p = int(input())
gates = [i*-1 for i in range(1,g+1)]
heapq.heapify(gates)
vis = set
for i in range(p):
    q = int(input())
    for j in range(g):
        a = heapq.heappop(gates)
        print(a)