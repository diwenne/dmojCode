x = int(input())
m = int(input())
bool = False
for n in range(m+1):
    if (x*n)%m ==1:
        print(n)
        bool = True
        break
if bool == False:
    print('No such integer exists.')