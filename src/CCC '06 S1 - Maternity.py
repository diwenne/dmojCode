parent1 = input()
parent2 = input()
q = int(input())
def babies(a1,a2,b1,b2):
    if a1 == a1.lower() and a2 == a2.lower():
        if b1 == b1.lower() and b2 == b2.lower():
            return [a1]
        elif b1 == b1.upper() and b2 == b2.lower():
            return [b1,b2]
        elif b1 == b1.upper() and b2 == b2.upper():
            return [b1]
    elif a1 == a1.upper() and a2 == a2.lower():
        if b1 == b1.lower() and b2 == b2.lower():
            return [a1,a2]
        elif b1 == b1.upper() and b2 == b2.lower():
            return [a1,a2]
        elif b1 == b1.upper() and b2 == b2.upper():
            return [b1]
    elif a1 == a1.upper() and a2 == a2.upper():
        if b1 == b1.lower() and b2 == b2.lower():
            return [a1]
        elif b1 == b1.upper() and b2 == b2.lower():
            return [a1]
        elif b1 == b1.upper() and b2 == b2.upper():
            return [a1]
def query():
    baby = input()
    for i in range(int(len(parent1)/2)):
        gene1 = parent1[2*i:2*i+2]
        gene2 = parent2[2*i:2*i+2]
        if baby[i] in babies(gene1[0],gene1[1],gene2[0],gene2[1]):
            continue
        else:
            print('Not their baby!')
            return

    print("Possible baby.")

for i in range(q):
    query()



