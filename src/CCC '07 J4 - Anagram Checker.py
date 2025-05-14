boolean = True
word1 = input()
word1copy = word1[:]
word2 = input()
word2copy = word2[:]
if len(word2)>len(word1):
    word1 = word2copy
    word2 = word1copy

if " " in word1:
    word1 = word1.replace(" ", "")
if " " in word2:
    word2 = word2.replace(" ", "")
word1 = list(word1)
word2 = list(word2)

for i in word1:

    # print(i)
    if i in word2:

        word2.remove(i)
        # print(word1, word2)
    else:
        boolean = False
        break

if boolean:
    print("Is an anagram.")
else:
    print("Is not an anagram.")
