import sys
startday, numday = map(int,input().split())
print("Sun Mon Tue Wed Thr Fri Sat")
if startday == 1:
    print("  1  ", end="")
if startday == 2:
    print("      1  ", end="")
if startday == 3:
    print("          1  ", end="")
if startday == 4:
    print("              1  ", end="")
if startday == 5:
    print("                  1  ", end="")
if startday == 6:
    print("                      1  ", end="")
if startday == 7:
    print("                          1", end="")
counter = 1
for i in range(8):
    counter+=1
    if counter + startday == 9:
        print()
        print(" ", end="")
    if counter + startday == 16:
        print()
        print(" ", end="")

    if counter+startday == 8:
        print(" " + str(counter), end="")
    elif counter+startday == 15:
        print(" " + str(counter), end="")
    elif i<8:
        print(" " + str(counter) + "  ", end="")

for i in range(numday-8):
    counter+=1
    if counter + startday == 16:
        print()
        print(" ", end="")
    if counter + startday == 23:
        print()
        print(" ", end="")
    if counter + startday == 30:
        print()
        print(" ", end="")
    if counter + startday == 37:
        print()
        print(" ", end="")
    if counter + startday == 15:
        print(str(counter), end="")
    elif counter + startday == 22:
        print(str(counter), end="")
    elif counter + startday == 29:
        print(str(counter), end="")
    elif counter + startday == 36:
        print(str(counter), end="")
    elif counter  == numday:
        print(str(counter), end="")

    else:
        print(str(counter) + "  ", end="")
    if counter == numday:
        break
print()
