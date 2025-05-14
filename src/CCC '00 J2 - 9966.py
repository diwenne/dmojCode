def myfunction(n):
    n = list(n)
    valid = ["1","0","8"]
    newN = []
    for i in range(1,len(n)+1):
        x = n[-i]
        if x in valid:
            newN.append(x)
        elif x == "6":
            newN.append("9")
        elif x == "9":
            newN.append("6")
        else:
            return 0
    if newN == n:
        return 1
    return 0
counter = 0
a = int(input())
b = int(input())
for i in range(a,b+1):
    # print(i)
    # print(myfunction(str(i)))
    counter+= myfunction(str(i))
print(counter)