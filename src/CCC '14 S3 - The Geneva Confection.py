from sys import exit
def solution():
    n = int(input())
    top = [0]
    branch = [0]
    for i in range(n):
        top.append(int(input()))

    for i in range(1,n+1):
        # print(i,69)
        while True:
            # print(top,branch)
            try:
                if top[-1] == i:
                    top.pop(-1)
                    break
            except IndexError:
                print('N')
                return

            if branch[-1] == i:
                branch.pop(-1)
                break
            else:
                branch.append(top.pop(-1))


    print('Y')

for i in range(int(input())):
    solution()