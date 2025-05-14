t = int(input())
n = int(input())
values = []
minvalues = []
for i in range(n):
    mins = int(input())
    values.append(mins)
while True:
    minimum = min(values)
    minvalues.append(minimum)
    values.remove(minimum)
    if sum(minvalues)>t:
        break
minvalues.pop()
print(len(minvalues))


