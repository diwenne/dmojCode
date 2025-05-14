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
    for i in range(q):
        a = die.randrange(2,n-1)
        if not single_test(n,a):
            # print(-1)
            return False
    # print(1)
    return True

# print(miller_rabin(97))
for i in range(int(input())):
    n = int(input())
    if n == 1:
        print("NOT")
    elif n == 0:
        print("NOT")
    elif n == 2:
        print("PRIME")
    elif n == 3:
        print("PRIME")
    elif miller_rabin(n):
        print("PRIME")
    else:
        print("NOT")
