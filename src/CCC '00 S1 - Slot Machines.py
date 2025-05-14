total = 0
m = int(input())
a = int(input())
b = int(input())
c = int(input())
while m:
    if m == 0:
        break
    total += 1
    m -= 1
    a += 1
    if a == 35:
        a=0
        m+=30


    if m == 0:
        break
    total += 1
    m -= 1
    b += 1
    if b == 100:
        b=0
        m+=60

    if m == 0:
        break
    total += 1
    m -= 1
    c += 1
    if c == 10:
        c=0
        m+=9
    print(total, m, a, b, c)

print("Martha plays", str(total), "times before going broke.")