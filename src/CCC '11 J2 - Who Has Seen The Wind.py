h = int(input())
m = int(input())
for t in range(1, m+1):
    a = -6*t**4 + h*t**3 + 2*t**2 + t
    if a<=0:
        print("The balloon first touches ground at hour:")
        print(t)
        break
    if t == m:
        print("The balloon does not touch ground in the given time.")
        break
#
# h = int(input())
# m = int(input())
# t = int(input())
# a = -6*t**4 + h*t**3 + 2*t**2 + t
# print(a)