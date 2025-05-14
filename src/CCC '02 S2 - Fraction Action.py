import math
nume = int(input())
deno = int(input())
numden = []
divisible = []
numden.append(nume)
numden.append(deno)
smallerOne = min(numden)
gcf = 1
if nume%deno==0:
    print(int(nume/deno))
elif nume == 1:
    print(str(nume) + "/" + str(deno))

else:
    for i in range(2, smallerOne+1):
        if nume%i == 0 and deno%i == 0:
            divisible.append(i)

        if len(divisible) == 0:
            gcf = 1
        else:
            gcf = max(divisible)
    nume = nume/gcf
    deno = deno/gcf
    if nume<deno:
        print(str(int(nume)) + "/" + str(int(deno)))
    if nume > deno:
        firstnum = math.floor(nume/deno)
        secondnu = nume%deno
        secondnum = str(int(secondnu)) + "/" + str(int(deno))
        mixed = str(firstnum) + " " + secondnum
        print(mixed)







