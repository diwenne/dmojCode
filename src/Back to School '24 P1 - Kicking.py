import copy
r,c,k = map(int,input().split())
graph = []
for i in range(r):
    line = list(input())
    graph.append(line)
graphcopy = copy.deepcopy(graph)
# print(graphcopy,graph)
# graphcopy[1][1] = 1
# print(graphcopy,graph)

for row in range(r):
    for col in range(c):

        bool = None
        # print(row,col)
        if graph[row][col] == "A":
            bool = True


            for i in range(1,3):
                if col+i<c:
                    # print(1)
                    if graph[row][col+i] == "B":
                        bool = False
            if bool == True:
                graphcopy[row][col] = "Y"
            if bool == False:
                # print(graph)
                graphcopy[row][col] = "N"
                # print(graph,row,col)
                # sys.exit()

        if graph[row][col] == "B":
            # print(row,col)
            bool = True


            for i in range(1,3):
                if col-i>-1:
                    # print(1)
                    # print(graph)
                    if graph[row][col-i] == "A":
                        bool = False
            if bool == True:
                graphcopy[row][col] = "Y"
            if bool == False:
                graphcopy[row][col] = "N"
for i in graphcopy:
    print("".join(i))
        # if bool == True:
        #     print(row,col,69)


