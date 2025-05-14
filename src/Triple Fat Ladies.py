for i in range(int(input())):
    k = int(input())
    counter = k
    def checker(num):
        numcube = num**3
        if str(numcube)[-3:] == "888":
            return True
        else:
            return False
    while 1:
        counter +=1
        if checker(counter):
            print(counter)
            break
        else:
            pass
    # while counter<30:
    #     counter+=1
    #     cubed = counter**3
    #     print(cubed)


