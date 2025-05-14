queries = []
for i in range(int(input())):
    a,b = map(int,input().split())
    queries.append((b,a))

n = max(queries)[0]
n+=1
primes = [True for _ in range(n)]


def soe(n):
    primes[0], primes[1] = False, False
    p = 2
    while p ** 2 < n:
        if primes[p]:
            for i in range(p ** 2, n, p):
                # print(i)
                primes[i] = False
        p += 1

    return [i for i in range(n) if primes[i] == True]



all_primes = set(soe(n))
# print(all_primes)
for b,a in queries:
    counter = 0
    for i in all_primes:
        # print(i)
        if a<=i<=b:
            counter +=i
    print(counter)



