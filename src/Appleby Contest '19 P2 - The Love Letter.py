n = int(input())
l = int(input())
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letter = list(input())
shiftedlist = []
for char in letter:
    if char.isalpha():
        ind = alphabet.index(char)
        newind = ind+l
        if newind>25:
            newind = newind%26
        shiftedlist.append(alphabet[newind])
    else:
        shiftedlist.append(' ')

print("".join(shiftedlist))

