n, k = map(int,input().split())
totalscore = {key:[] for key in range(n+1)}

for i in range(k):
    scores = list(map(int,input().split()))
    for i in range(n):
        totalscore[i+1]+=scores[i]
    print(scores)

