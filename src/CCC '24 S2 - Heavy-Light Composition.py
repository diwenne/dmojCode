t,f = map(int,input().split())
def check(letters):
    heavy = set()
    for i in letters:
        if letters.count(i) > 1:
            heavy.add(i)

    if letters[0] in heavy:
        bool = True
    else:
        bool = False
    for i in letters:
        if bool == True:
            if i in heavy:
                bool = False
                continue
            else:
                print('F')
                return

        if bool == False:
            if i not in heavy:
                bool = True
                continue
            else:
                print('F')
                return
    print('T')
    return
for i in range(t):
    letters = list(input())
    check(letters)
