verses = int(input())
for i in range(verses):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    verse1 = str(input())
    verse2 = str(input())
    verse3 = str(input())
    verse4 = str(input())

    def find_end(verse):
        for i in range(1, len(verse) +1):
            if verse[-i] in vowels:
                return verse[-i:len(verse)]
            elif i>1 and verse[-i] == " ":
                return verse[-i+1:len(verse)]

            elif i == len(verse):
                return verse

    sylVerse1 = find_end(verse1).upper()
    sylVerse2 = find_end(verse2).upper()
    sylVerse3 = find_end(verse3).upper()
    sylVerse4 = find_end(verse4).upper()

    # if sylVerse1 == sylVerse2 == sylVerse3 == sylVerse4 == "na":
    #     print("free")
    # elif sylVerse1 == "na" or sylVerse2 == "na" or sylVerse3 == "na" or sylVerse4 == "na":
    #     print("free")
    if sylVerse1 == sylVerse2 == sylVerse3 == sylVerse4:
        print("perfect")
    elif sylVerse1 == sylVerse2 and sylVerse3 == sylVerse4:
        print("even")
    elif sylVerse1 == sylVerse3 and sylVerse2 == sylVerse4:
        print("cross")
    elif sylVerse1 == sylVerse4 and sylVerse2 == sylVerse3:
        print("shell")
    else:
        print("free")

    print(sylVerse1)
    print(sylVerse2)
    print(sylVerse3)
    print(sylVerse4)




