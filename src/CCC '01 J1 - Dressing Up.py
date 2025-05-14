h = int(input())
half_h = int((h+1)/2)
counter = 1
# print(half_h)
for iter in range(half_h):

    spaces = h*2 - counter*2
    for i in range(counter):
        print("*",end="")
    for i in range(spaces):
        print(" ",end="")
    for i in range(counter):
        print("*",end="")
    counter+=2
    print("")
counter -=2
while counter >= 1:
    # print(counter)
    counter = counter - 2
    spaces = h*2 - counter*2

    for i in range(counter):
        print("*", end="")
    for i in range(spaces):
        print(" ", end="")
    if counter>=3:
        for i in range(counter):
            print("*", end="")
        print("")
    if counter == 1:
        print("*")