fulltime = input()
hour = int(fulltime[:2])
min = int(fulltime[-2:])
mins = min+hour*60


for i in range(120):
    if 420<=mins<600:
        mins+=2
    elif 900<=mins<1140:
        mins+=2
    else:
        mins+=1
print(str((mins//60)%24).zfill(2)+':'+str(mins%60).zfill(2))






