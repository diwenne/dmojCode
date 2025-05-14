min = int(input())
def arithCheck(time):
    time=str(time)
    for i in range(1,len(time)-1):
        if int(time[i])-int(time[i-1])!=int(time[i+1])-int(time[i]):
            return False
    return True
counter = 0
halfdays = min//720
min=min%720
# print(min)
for i in range(min+1):
    hour = (12+i//60)%12 or 12
    min = 0+i%60
    if min<10:
        min = "0"+str(min)
    if arithCheck(str(hour)+str(min)):
        counter+=1
        print(hour,min)

print(counter+halfdays*31)