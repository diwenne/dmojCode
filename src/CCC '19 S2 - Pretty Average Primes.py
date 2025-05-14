import random
import sys
die = random.SystemRandom()
#false = prime, true = comp
def single_test(n,a):
    # print(n,a)
    exp = n-1
    while not exp & 1: # while even
        exp >>= 1 # divide by 2

    if pow(a,exp,n) == 1:
        # print(10)
        return True

    while exp<n-1:
        if pow(a,exp,n) == n-1:
            # print(11)
            return True
        exp<<=1

    # print(12)
    return False

def miller_rabin(n,q = 40):
    if n == 2 or n == 3:
        return True

    for i in range(q):
        a = die.randrange(2,n-1)
        if not single_test(n,a):
            # print(-1)
            return False
    # print(1)
    return True
def sum(n):
# print(miller_rabin(97))


    for i in range(2,n-1):
        a,b = i,n-i
        # print(a,b)
        if miller_rabin(a) and miller_rabin(b):
            print(a,b)
            return

for _ in range(int(input())):
    sum(int(input()))
