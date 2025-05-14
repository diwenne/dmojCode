t = int(input())
g = int(input())
points = [0 for _ in range(5)]
match_ups = [(1,2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
distr = [(1,1),(0,3),(3,0)]
for i in range(g):
    t1,t2,s1,s2 = map(int,input().split())
    if s1 > s2:
        points[t1] = points[t1]+3
    elif s1 < s2:
        points[t2] = points[t2]+3
    elif s1==s2:
        points[t1] += points[t1]+1
        points[t2] +=points[t2]+1
    print((t1,t2))
    match_ups.remove((t1,t2))
alldata = []


# for i in range((6-g)**3):
#     data = []
#     for team1,team2 in match_ups:
#         for p1,p2 in distr:
#             data.append((team1,p1,team2,p2))
#     alldata.append(data)
# print(data)
#
#
#
# print(match_ups)
# print(points)

