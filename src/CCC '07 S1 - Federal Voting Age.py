for i in range(int(input())):
    y,m,d = map(int,input().split())
    if y<1989:
        print('Yes')
    if y==1989:
        if m<2:
            print('Yes')
        if m==2:
            if d<=27:
                print('Yes')
            if d>27:
                print('No')
        if m>2:
            print('No')
    if y>1989:
        print('No')