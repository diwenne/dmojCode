daytime = int(input())
evening = int(input())
weekend = int(input())

priceAD = (daytime-100)*0.25
if priceAD < 0:
    priceAD += priceAD*(-1)
priceAE = evening*0.15
priceAW = weekend*0.2

priceBD = (daytime-250)*0.45
if priceBD < 0:
    priceBD += priceBD*(-1)
priceBE = evening*0.35
priceBW = weekend*0.25

planA = round((priceAD + priceAE + priceAW), 2)
planB = round((priceBD + priceBE + priceBW), 2)
if planA == 59.0:
    print ("Plan A costs 59.00")
if not planA == 59.0:
    print("Plan A costs ", + planA)
if planB == 37.0:
    print ("Plan B costs 37.00")
if not planB == 37.0:
    print("Plan B costs ", + planB)
# print("Plan A costs ", + planA)
# print("Plan B costs ", + planB)

if planA < planB:
    print("Plan A is cheapest.")
elif planB < planA:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")


