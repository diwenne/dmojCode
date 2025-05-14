r = int(input())
c = int(input())
k = int(input())
strokes = []
hori = set()
vert = set()
for i in range(k):
    rc, a = input().split()
    if rc == 'R':
        if (rc,a) in hori:
            hori.remove((rc,a))
        else:
            hori.add((rc,a))
    else:
        if (rc,a) in vert:
            vert.remove((rc,a))
        else:
            vert.add((rc,a))
counter = len(hori)*c+len(vert)*r-len(hori)*(len(vert)*2)
print(counter if counter>=0 else 0)






