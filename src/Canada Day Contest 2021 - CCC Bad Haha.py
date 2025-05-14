import heapq
for i in range(int(input())):
    n = list(input())
    n = list(map(int,n))
    # print(n)
    remdig = []
    k = int(input())
    if k>len(n):
        k = len(n)
    # print(k)
    # print(k)
    for i in range(k):
        # print(k)
        # print(i)
        # boo = False
        for j in range(len(n)+len(remdig)):
            # print(j)
            if j<len(n)-1:
                # print(j,69)
                # print(n)
                if n[j]>n[j+1]:

                    heapq.heappush(remdig,n[j])
                    # print(remdig)
                    # print(n)
                    n.pop(j)
                    # print(k)
                    # k-=1
                    break
            elif j >=len(n)-1:
                # print(j,70)
                if n[-1]>remdig[0]:
                    heapq.heappush(remdig,n[-1])
                    n.pop(-1)
                    # print(k)
                    # k-=1
                    break
    # print(remdig)
    for i in range(len(remdig)):
        a = heapq.heappop(remdig)
        n.append(a)

    n = list(map(str,n))
    print("".join(n))


    # print(remdig)
