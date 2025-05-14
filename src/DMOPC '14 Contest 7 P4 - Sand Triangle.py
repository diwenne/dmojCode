n = int(input())
row  = 1
firstnum = 1
while True:
    if firstnum<=n and n<= firstnum+row-1:
        print(int((firstnum+firstnum+row-1)*row/2))
        break
    firstnum += row
    row+=1
