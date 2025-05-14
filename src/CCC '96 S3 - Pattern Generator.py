t = int(input())
for i in range(t):

    n,k = map(int,input().split())
    print('The bit patterns are')
    def generator(depth, ones,pattern):

        if ones>k:
            return

        if depth ==n:
            if ones == k:
                print(pattern)
                return
            return

        if depth<n:
            generator(depth+1,ones+1, pattern+'1')
            generator(depth+1,ones, pattern+'0')
        # print(allList)


    generator(0,0,'')
    if i != t-1:
        print()


