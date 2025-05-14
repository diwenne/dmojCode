teama3 = int(input())
teama2 = int(input())
teama1 = int(input())
teamb3 = int(input())
teamb2 = int(input())
teamb1 = int(input())

a = teama3*3+teama2*2+teama1
b = teamb3*3+teamb2*2+teamb1
if a > b:
    print("A")
if a < b:
    print("B")
if a == b:
    print("T")

