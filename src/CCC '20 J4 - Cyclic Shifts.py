t = input()
s = input()

shifts = [s]
def shifted(s):
    return s[-1]+s[:-1]

for i in range(len(s)-1):
    shifts.append(shifted(shifts[-1]))

def check():
    for i in shifts:
        if i in t:
            return 'yes'
    return 'no'

print(check())