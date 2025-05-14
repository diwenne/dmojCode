n = int(input())
scorelist = []
namelist = []
for i in range(n):
    name, r, s, d =  input().split()
    namelist.append(name)
    r = int(r)
    s = int(s)
    d = int(d)
    score = 2*r+3*s+d
    scorelist.append(score)
if len(namelist) == 1:
    print(namelist[0])
elif len(namelist) > 1:
    for i in range(2):
        maxi = scorelist.index(max(scorelist))
        print(namelist[maxi])
        scorelist.remove(scorelist[maxi])
        namelist.remove(namelist[maxi])
