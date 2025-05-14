est = int(input())
pst = est - 300
mst = est - 200
cst = est - 100
ast = est + 100
nflst = est + 130


if est < 0:
    print(2400 + est, end="")
    print(" in Ottawa")
else:
    print(est, end="")
    print(" in Ottawa")
if pst < 0:
    print(2400 + pst, end="")
    print(" in Victoria")
else:
    print(pst, end="")
    print(" in Victoria")
if mst < 0:
    print(2400 + mst, end="")
    print(" in Edmonton")
else:
    print(mst, end="")
    print(" in Edmonton")
if cst < 0:
    print(2400 + cst, end="")
    print(" in Winnipeg")
else:
    print(cst, end="")
    print(" in Winnipeg")
if est < 0:
    print(2400 + est, end="")
    print(" in Toronto")
else:
    print(est, end="")
    print(" in Toronto")
if ast < 0:
    print(2400 + ast, end="")
    print(" in Halifax")
else:
    print(ast, end="")
    print(" in Halifax")

def conv(nflst):
    nflsts = str(nflst)[-2:]
    if int(nflsts)<60:
        return nflst
    if int(nflsts)>=60:
        nflst += 40
        return nflst
nflst2 = conv(nflst)
if nflst2 < 0:
    print(2400 + nflst2, end="")
    print(" in St John's")
else:
    print(nflst2, end="")
    print(" in St. John's")







