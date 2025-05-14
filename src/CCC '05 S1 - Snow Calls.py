n = int(input())
dict = {
    "A":2,
    "B":2,
    "C":2,
    "D":3,
    "E":3,
    "F":3,
    "G":4,
    "H":4,
    "I":4,
    "J":5,
    "K":5,
    "L":5,
    "M":6,
    "N":6,
    "O": 6,
    "P": 7,
    "Q": 7,
    "R": 7,
    "S": 7,
    "T": 8,
    "U": 8,
    "V": 8,
    "W": 9,
    "X": 9,
    "Y": 9,
    "Z": 9,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "0":0,

}
for i in range(n):
    rawnum = input()
    rawnum = rawnum.replace("-", "")

    rawnum = list(rawnum)
    for j in range(len(rawnum)):
        rawnum[j] = dict[rawnum[j]]
    rawnum.insert(3, "-")
    rawnum.insert(7, "-")
    if len(rawnum)>12:
        for i in range(len(rawnum)-12):
            rawnum.pop(-1)
    newnum = map(str, rawnum)

    newnum = "".join(newnum)
    print(newnum)




