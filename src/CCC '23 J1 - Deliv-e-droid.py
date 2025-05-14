d = int(input())
c = int(input())
score = d*50-c*10
if d > c:
    score += 500
print(score)