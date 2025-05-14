total = int(input())
scores = set()
lis = []
for i in range(total):
    score = int(input())
    scores.add(score)
    lis.append(score)
scores = list(scores)
scores.sort(reverse = True)
bronze = scores[2]
print(bronze, end=" ")
counter = 0
for i in lis:
    if i == bronze:
        counter+=1
print(counter)

