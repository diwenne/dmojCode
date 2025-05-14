winCounter = 0
for i in range(6):
    result = input()
    if "W" in result or "w" in result:
        winCounter += 1
if winCounter >= 5:
    print(1)
elif winCounter >= 3 and winCounter < 5:
    print(2)
elif winCounter >= 1 and winCounter < 3:
    print(3)
elif winCounter < 1:
    print(-1)