from collections import deque

def afunction(word, inde):
    letter = word[inde]
    counter = 0
    while True:
        inde+=1
        if word[inde]== letter:
            counter+=1
        else:
            break
    return counter
def indexx(word,letter):
    counter = 0
    a = afunction(word, 0)
    for i in range(len(word)):
        if word[i] == letter:
            ind = i
            while ind+1<len(word):

                ind+=1
                if word[ind] == letter:
                    continue
                else:
                    return ind-1
    return ind

print(afunction("BBASNBASSNA",0))
while True:
    w = input()
    if w == "X":
        break
    queue = deque([w])


    def find(w):
        while queue:
            word = queue.popleft()
            print(word)
            if "A" not in word:
                return False
            if word == 'A':
                # print(1)
                continue
            else:

                #N can only connect 2 monkey words
                if word[0] == "N" or word[-1] == "N":
                    return False
                #if B and S are at start and end
                if word[0] == "B" and "S" in word:
                    # print(3)
                    a = indexx(word, "S")
                    # print(a)
                    queue.append(word[1:a])
                    if len(word)>a+1:
                        # print(a)

                        if word[a+1] != "N":
                            # print(-1)
                            return False
                        else:
                            queue.append(word[a+2:])
                    continue
                elif "N" in word:
                    # print(4)
                    a = word.index("N")
                    # print(a)
                    queue.append(word[:a])
                    queue.append(word[a+1:])
                else:
                    return False


    if find(w) == None:
        print("YES")
    else:
        print("NO")
