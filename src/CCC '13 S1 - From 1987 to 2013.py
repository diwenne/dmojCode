y = int(input()); y+=1
while True:
    distinct = set(str(y))
    if len(distinct) == len(str(y)):
        print(y)
        break
    y+=1
