n = int(input())
i = 0
counter = 0
while i*4<=n:
    number = i*4
    # print(number)
    if (n - number) % 5 == 0:
        counter += 1
        # print(i,69)
    i+=1
print(counter)