fword = input()
swordcopy = input()
sword = swordcopy+'              '
hasquiet=False
samelength = False
#find sillykey
for i in swordcopy:
    if i in fword:
        pass
    else:
        sillykey = i
# print(sillykey)
#find quiet
if len(fword) == len(swordcopy):
    samelength = True
    quiet = '-'

else:
    for i in range(len(fword)):
        if fword[i] == sword[i]:
            pass
        elif sword[i] == sillykey:
            pass
        else:
            quiet = fword[i]
            hasquiet = True
            break
# print(quiet)
#find correctkey
for i in fword:
    if i not in sword:
        if i == quiet:
            pass
        else:
            correct = i
            break
# print(correct)
print(correct, sillykey)
print(quiet)

# print(a, f)
# print(s)
