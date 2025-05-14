t = int(input())
s = int(input())
h = int(input())
for i in range(t):
    print("*",end="")
    for j in range(s):
        print(" ",end="")
    print("*",end="")
    for k in range(s):
        print(" ",end="")
    print("*")
for l in range(3+s*2):
    print("*",end="")
print("")
for m in range(h):
    for n in range(1+s):
        print(" ",end="")
    print("*")