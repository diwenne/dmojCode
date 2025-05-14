n = int(input())
people = []
for i in range(n):
    people.append(int(input()))
counter = 0
for i in range(n):
    opposite = int(i+n/2)
    if opposite >n-1:
        opposite = int(opposite%n)
    if people[i]==people[opposite]:
        counter+=1
print(counter)
