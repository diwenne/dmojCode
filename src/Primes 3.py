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

def miller_rabin(n,q =2):
    for i in range(q):
        a = die.randrange(2,n-1)
        if not single_test(n,a):
            # print(-1)
            return False
    # print(1)
    return True

# print(miller_rabin(97))
for i in range(int(input())):
    number = int(input())
    notprime = [0,1]
    isprime = [2,3]
    if number in notprime:
        print("NOT")
    elif number in isprime:
        print('PRIME')
    else:
        if miller_rabin(number):
            print("PRIME")

        else:
            print("NOT")
