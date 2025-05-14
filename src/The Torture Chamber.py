import math
def sieve(limit):
    primes = [True for _ in range(limit+1)]
    primes[0],primes[1] = False, False
    p = 2
    while p*p <= limit:
        if primes[p] == True:
            for i in range(p*p,limit+1,p):
                primes[i] = False
        p +=1
    return [i for i in range(limit+1) if primes[i]]

def segmented(low,high):
    limit = int(math.sqrt(high))+1
    primes = sieve(limit)
    all_primes = [True for _ in range(high-low+1)]
    # print(primes)
    for prime in primes:
        start = max(prime*prime, low+(prime-low%prime)%prime)
        for i in range(start,high+1,prime):
            all_primes[i-low] = False

    prime_nums = [num for num, boo in zip(range(low,high+1),all_primes) if boo and num>1]
    return prime_nums
a = int(input())
b = int(input())
b-=1
prime_nums = segmented(a,b)
print(len(prime_nums))