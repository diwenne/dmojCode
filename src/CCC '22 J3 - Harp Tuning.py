ins = str(input())
ins = ins+' '
cmds = 0
cmdsindex = []
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
nums = list(map(str, nums))
digits = []

for i in range(len(ins)):
    if ins[i] == "+" or ins[i] == "-":
        cmds+=1
        cmdsindex.append(i)

y = 1

for i in range(len(cmdsindex)):
    y = 1
    x = cmdsindex[i]
    # print(x, y)
    while ins[x+y] in nums:
        y += 1
    y=y-1
    digits.append(y)


startpoint = 0
for i in range(cmds):
    print(ins[startpoint:cmdsindex[i]], end="")
    if ins[cmdsindex[i]] == "+":
        print(" tighten ",end="")
    elif ins[cmdsindex[i]] == "-":
        print(" loosen ",end="")
    print(int(ins[cmdsindex[i]+1:cmdsindex[i]+1+digits[i]]))

    startpoint = cmdsindex[i]+1+digits[i]



# ins = str(input())
# cmds = 0
# cmdsindex = []
# turnsdigits= 1
# list = []
# a = 0
# for i in range(len(ins)):
#     if ins[i] == "+" or ins[i] == "-":
#         cmds+=1
#         cmdsindex.append(i)
# print(ins[cmdsindex[a]+i+1])
# #for each set of ins
# for i in range(len(cmdsindex)):
#
#     for k in range(len(ins)):
#
#         if ins[cmdsindex[a]+i+1]== int:
#             turnsdigits+=1
#             print(ins[cmdsindex[i]+1])
#         elif not ins[cmdsindex[a]+1+i] == int:
#             list.append(turnsdigits)
#             break
#     turnsdigits = 1


#
# print(list)
#
#
# startpoint = 0
# for i in range(cmds):
#     print(ins[startpoint:cmdsindex[i]], end="")
#
#     if ins[cmdsindex[i]] == "+":
#         print(" tighten ",end="")
#     elif ins[cmdsindex[i]] == "-":
#         print(" loosen ",end="")
#     startpoint = cmdsindex[i] + 2
#     print(ins[ cmdsindex[i]+1 ])


# print(cmdsindex)


