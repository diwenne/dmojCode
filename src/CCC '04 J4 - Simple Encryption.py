key = input()
msg = input()
def onlyalpha(string):
    result = ''
    for i in string:
        if i.isalpha():
            result+=i
    return result
msg = onlyalpha(msg)

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
def shift(letter, shiftletter):
    return alphabet[(alphabet.index(letter)+alphabet.index(shiftletter))%26]

result = ''
for i in range(len(msg)):
    keyletter = key[i%len(key)]
    result+=shift(msg[i],keyletter)
print(result)

