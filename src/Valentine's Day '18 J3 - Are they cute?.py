# from collections import deque
# import math
# import sys
# n = int(input())
# names = []
# cutes = []
# if n  < 3:
#     for i in range(n):
#         name,cute = input().split()
#         print(name+" is not cute. </3")
#     sys.exit()
# cutedata = {}
# for i in range(n):
#     name,cute = input().split()
#     cute = int(cute)
#     cutedata.setdefault(cute,[]).append(name)
#     names.append(name)
#     cutes.append(cute)
# allowed =n-  math.ceil((n+0.001)/2)
# arecute = []
# cutes.sort(reverse=True)
# while allowed>0:
#     a = cutes.pop(0)
#     for i in cutedata[a]:
#         arecute.append(i)
#         allowed-= 1
# for i in names:
#     if i in arecute:
#         print(i+" is cute! <3")
#     else:
#         print(i+" is not cute. </3")

# print(cutedata)
# print(arecute)


# import sys
# import math
# tppl = int(input())
# cutelist = []
# namelist = []
# newcutelist = []
# dict = {}
#
# for i in range(tppl):
#     name, cute = map(str, input().split())
#     cute = int(cute)
#     cutelist.append(cute)
#     namelist.append(name)
#     newcutelist.append(cute)
#     dict[cute]=name
#
# # if len(cutelist) == 2:
# #     for i in range(2):
# #         print(namelist[i], "is not cute. </3")
# #     sys.exit()
# if len(cutelist)/2 %1 == 0:
#     req = len(cutelist)/2 -1
# elif not len(cutelist)/2 %1 == 0:
#     req = math.floor(len(cutelist)/2)
# req = int(req)
#
#
# cutelist.sort(reverse=True)
# for i in range(tppl-req):
#     cutelist.pop(-1)
#
#
# for i in range(tppl):
#     if newcutelist[i] in cutelist:
#         print(dict[newcutelist[i]], "is cute! <3")
#     elif not newcutelist[i] in cutelist:
#         print(dict[newcutelist[i]], "is not cute. </3")



# print(cutelist)
# print(dict)






# # import math
# # numofpeople = int(input())
# # list  = []
# # cutelist = []
# # for i in range(numofpeople):
# #     name, cuteness = map(str, input().split())
# #     cuteness = int(cuteness)
# #     # name = str(input())
# #     # cuteness = int(input())
# #     namecute = [name, cuteness]
# #     list.append(namecute)
# # cutechecke = 1
# # if len(list) == 1 or len(list) == 2:
# #     print("not cute")
# #
# # elif len(list)>2:
# #     cutechecke = len(list)/2
# #
# # if cutechecke%1==0:
# #     cutechecke += 1
# # elif not cutechecke%1==0:
# #     cutechecke = math.ceil(cutechecke)
# # cutechecke = int(cutechecke)
# # list_nums = []
# # dict = {}
# # counter = 0
# # for i in range(numofpeople):
# #     numberinlist = list[counter][1]
# #     wordinlist = list[counter][0]
# #     counter+=1
# #     dict[numberinlist] = wordinlist
# #     list_nums.append(numberinlist)
# #
# #
# # for i in range(numofpeople-cutechecke):
# #     biginlist = max(list_nums)
# #     list_nums.remove(biginlist)
# #     cutelist.append(biginlist)
# #     # if i == numofpeople-cutechecke-1:
# #     #     while True:
# #     #         if biginlist in list_nums:
# #     #             cutelist.append(max(list_nums))
# #     #             list_nums.remove(biginlist)
# #     #         if not biginlist in list_nums:
# #     #             break
# # for i in range(len(cutelist)):
# #     cutelist[i] = dict[cutelist[i]]
# # for i in range(len(cutelist)):
# #     print(cutelist[i],end="")
# #     print(" is cute! <3")
# # for i in range(len(list_nums)):
# #     list_nums[i] = dict[list_nums[i]]
# # for i in range(len(list_nums)):
# #     print(list_nums[i],end="")
# #     print(" is not cute! <3")
# #
#
# #
# #
# #
# # # def diwen(x):
# # #     return dict[x]
# # # strcutelist = (map(diwen, cutelist))
# # # strcutelist = diwen(cutelist)
# # print(cutelist)
# # # print(len(strcutelist))
# # # print(cutelist)
# # print(list)
# # # print(dict)
# # # print(cutechecke)
# import sys
# import math
# numofpeople = int(input())
# namelist = []
# cutelist = []
# cutestlist = []
# namelistcopy=[]
# for i in range(numofpeople):
#     name, cuteness = map(str, input().split())
#     cuteness = int(cuteness)
#     namelist.append(name)
#     namelistcopy.append(name)
#     cutelist.append(cuteness)
#
#
#
#
# cutechecke = 1
# # if len(cutelist) == 1:
# #     print(namelist[0] + " is not cute. </3")
# #     sys.exit()
# if len(cutelist) == 2:
#     for i in range(2):
#         print(namelist[i] + " is not cute. </3")
#     sys.exit()
#
# elif len(cutelist)>2:
#     cutechecke = len(namelist)/2
# if cutechecke%1==0:
#     cutechecke += 1
# elif not cutechecke%1==0:
#     cutechecke = math.ceil(cutechecke)
# cutechecke = int(cutechecke)
#
#
# for i in range(numofpeople-cutechecke):
#     maxindex = cutelist.index(max(cutelist))
#     cutestlist.append(namelist[maxindex])
#     namelist.remove(namelist[maxindex])
#     cutelist.remove(cutelist[maxindex])
#
#
#
# for i in range(numofpeople):
#     if namelistcopy[i] in cutestlist:
#         print(namelistcopy[i] + " is cute! <3")
#     elif not namelistcopy[i] in cutestlist:
#         print(namelistcopy[i] + " is not cute. </3")
#
# # print(cutestlist)
# # print(cutelist)


# n = [1,2]
# c = [1,2]




n = int(input())
cutes = []
names=[]

for i in range(n):
    name, cute = input().split()
    cute = int(cute)
    cutes.append(cute)
    names.append(name)
sort = sorted(cutes)
# print(cutes)
for i in range(n):

        print(names[i]+" is cute! <3")
    else:
        print(names[i]+" is not cute. </3")






