rows,cols,k = map(int,input().split())
tempcounter = 0
highest_block = {}
for i in range(k):
    r,c = map(int,input().split())
    try:
        if c >highest_block[r]:

                highest_block[r] = c
                tempcounter+=1

        else:

            tempcounter += 1
    except:
        highest_block[r] = c

counter = sum(highest_block.values())
# print(highest_block,tempcounter)
if counter-tempcounter<0:
    print(0)
else:
    print(counter-tempcounter)


