p,g,r,o = int(input()),int(input()),int(input()),int(input())
sum = int(input())
def combinations(sum):
    global mincombo
    mincombo = float('inf')
    combos = []
    for pink in range(sum//p+1):
        for green in range(sum//g+1):
            for red in range(sum//r+1):
                for orange in range(sum//o+1):
                    if pink*p+orange*o+green*g+red*r == sum:
                        combos.append((pink,green,red,orange))
                        mincombo = min(mincombo, pink+green+orange+red)

    return combos
combos = combinations(sum)

for pink,green,red,orange in combos:
    print(f'# of PINK is {pink} # of GREEN is {green} # of RED is {red} # of ORANGE is {orange}')
print(f'Total combinations is {len(combos)}.')
print(f'Minimum number of tickets to print is {mincombo}.')


