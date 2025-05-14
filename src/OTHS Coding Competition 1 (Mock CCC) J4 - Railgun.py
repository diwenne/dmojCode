n,s,t = map(int,input().split())
robots = list(map(int,input().split()))

def prefix_sum(lis):
    sums = [[]for _ in range((n))]
    sums[0] = robots[0]
    for i in range(1,n):
        # print(sum(robots[i*s:i*s+s]))
        sums[i]=sums[i-1]+robots[i]
    return sums

lSums = prefix_sum(robots)
rSums = prefix_sum(robots.reverse())




prefix_sum(robots)
values = []

if t*s>=n:
    print(sum(robots))

else:
    for i in range(t+1):
        tRight = i
        tLeft = t-i
        # print(rSums)
        rPower = rSums[s * tRight -1] if tRight > 0 else 0
        lPower = lSums[s * tLeft -1] if tLeft > 0 else 0
        # print(rPower,lPower)

        values.append(rPower+lPower)

    print(max(values))


