for i in range(1,int(input())+1):
    word = input()
    num = int(word[:1])
    # print(num)
    word = list(word[2:])
    # print(word)
    word.pop(num-1)
    print(i,"".join(word))

