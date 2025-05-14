a = int(input())
b = int(input())
i = 1
counter = 0
while True:
    if a<= i**6 <=b:
        counter +=1
    if i**6 >b:
        break
    i+=1
print(counter)