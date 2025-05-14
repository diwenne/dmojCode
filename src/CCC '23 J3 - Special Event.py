guests = int(input())
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
for i in range(guests):
    avbl = input()
    if avbl[0:1] == "Y":
        counter1 += 1
    if avbl[1:2] == "Y":
        counter2 += 1
    if avbl[2:3] == "Y":
        counter3 += 1
    if avbl[3:4] == "Y":
        counter4 += 1
    if avbl[4:5] == "Y":
        counter5 += 1
biggest = max(counter1, counter2, counter3, counter4, counter5)
list =[]
if counter1 == biggest:
    list.append("1")
if counter2 == biggest:
    list.append("2")
if counter3 == biggest:
    list.append("3")
if counter4 == biggest:
    list.append("4")
if counter5 == biggest:
    list.append("5")
print(",".join(list))
# print(counter1)
# print(counter2)
# print(counter3)
# print(counter4)
# print(counter5)
