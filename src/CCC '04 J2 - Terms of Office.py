first = int(input())
second = int(input())
years = []
while first<=second:
    years.append(first)
    first+=60
for i in years:
    print("All positions change in year", i)