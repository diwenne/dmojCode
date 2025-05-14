# word = str
# while not word == "quit!":
#     word = str(input())
#     if len(word) >= 4 and "or" in word:
#         wordi = word.index("or")
#         newWord = word[0:wordi] + "our" + word[wordi + 2:len(word) + 1]
#         print(newWord)
#     elif word == "quit!":
#         break
#     else:
# #         print("word")
# vowel = "a" or "u" or "e" or "i" or "o"
word = str
while not word == "quit!":
    word = str(input())
    if len(word) >= 4 and "or" in word[-2:]:
        cons = word[-3:-2]
        if cons.startswith(("a", "e", "i", "o", "u")):
            print(word)
        if not cons.startswith(("a", "e", "i", "o", "u")):
            print(word.replace("or", "our"))
    elif word == "quit!":
        break
    else:
        print(word)
#








