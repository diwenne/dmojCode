n,k = map(int,input().split())
seq = input()
def factorial(n):
    if n ==1:
        return 1
    return n*factorial(n-1)

if k ==1:
    print(factorial(len(seq))*26*k-1)

