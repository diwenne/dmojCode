# def search(self, state, g_score):
#     cube = RubiksCube(state=state)
#     if cube.solved():
#         return True
#     elif len(self.moves) >= self.threshold:
#         return False
#     min_val = float('inf')
#     best_action = None
#     for a in [(r, n, d) for r in ['h', 'v', 's'] for d in [0, 1] for n in range(cube.n)]:
#         cube = RubiksCube(state=state)
#         if a[0] == 'h':
#             cube.horizontal_twist(a[1], a[2])
#         elif a[0] == 'v':
#             cube.vertical_twist(a[1], a[2])
#         elif a[0] == 's':
#             cube.side_twist(a[1], a[2])
#         if cube.solved():
#             self.moves.append(a)
#             return True
#         cube_str = cube.stringify()
#         h_score = self.heuristic[cube_str] if cube_str in self.heuristic else self.max_depth
#         f_score = g_score + h_score
#         if f_score < min_val:
#             min_val = f_score
#             best_action = [(cube_str, a)]
# #         elif f_score == min_val:
# #             if best_action is None:
# #                 best_action = [(cube_str, a)]
# #             else:
# #                 best_action.append((cube_str, a))
# #     if best_action is not None:
# #         if self.min_threshold is None or min_val < self.min_threshold:
# #             self.min_threshold = min_val
# #         next_action = choice(best_action)
# #         self.moves.append(next_action[1])
# #         status = self.search(next_action[0], g_score + min_val)
# #         if status: return status
# #     return False
# # search(input())
# # node = (1, 2)
# # x,y = node
# # print(x+ y)
#
# # arr = [
# # [1 2 3 54 6],
# # [43 4 2 5 1],
# # ]
# # for i in range(len(arr)):
# #     arr[i].replace("", ",")
# # for i in arr:
# #     print(i)
# # array = []
# # for i in range(3):
# #     array.append(list(map(int,input().split())))
# # print (array)
# r = int(input())
# c = int(input())
# arr = []
# adj = {}
# end = (r-1, c-1)
# for i in range(r):
#     arr.append(list(map(int, input().split())))
# # for i in range(r):
# #     for j in range(c):
# #         adj[i,j] = []
# print(adj)
# for i in range(r):
#     for j in range(c):
#         a = i*j
#         for t in range(r):
#             for p in range(c):
#                 if arr[t][p] == a:
# #                     adj.setdefault((i,j), []).append([t,p])
# # print(adj)
#
# # a = 1+1 = 5
# # pr
# # int(a)
# def pop(x):
#     return x+3
# a = pop(2)
# print(a)
# import sys
# int(input())
# a = list(input())
# boou = False
# boot = False
# good = ["A","G","U","T","C"]
# for i in a:
#     if i in good:
#         if i == "U":
#             boou = True
#         if i == "T":
#             boot = True
#     else:
#         print("neither")
#         sys.exit()
#
# if boot == True and boou == True:
# #     print("neither")
# # elif boot == True:
# #     print("DNA")
# # elif boou == True:
# #     print("RNA")
# # elif boou == False and boot == False:
# import sys
# sys.setrecursionlimit(100000)
# v = int(input())
# e = v-1
# adj = [[]for _ in range(v+1)]
# for i in range(1,e+1):
#     a,b = map(int,input().split())
#     adj[a].append(b)
# nodedata=[0 for _ in range(v+1)]
# def dp(node):
#     # print(node,69)
#
#     if nodedata[node]!= 0:
#         return nodedata[node]
#     maxlength = 0
#     for i in adj[node]:
#         print(node,i)
#         maxlength = max(maxlength,dp(i))
#     nodedata[node] = maxlength + 1
#     # print(maxlength)
#     return nodedata[node]
# # for i in range(1,v+1):
# #     dp(i)
# # print(nodedata)
# # print(max(nodedata))
# h = int(input())
# half_h = int((h+1)/2)
# counter = 1
# # print(half_h)
# for iter in range(half_h):
#
#     spaces = h*2 - counter*2
#     for i in range(counter):
#         print("*",end="")
#     for i in range(spaces):
#         print(" ",end="")
#     for i in range(counter):
#         print("*",end="")
#     counter+=2
#     print("")
# counter -=2
# while counter >= 1:
#     # print(counter)
#     counter = counter - 2
#     spaces = h*2 - counter*2
#
#     for i in range(counter):
#         print("*", end="")
#     for i in range(spaces):
#         print(" ", end="")
#     if counter>=3:
#         for i in range(counter):
#             print("*", end="")
#         print("")
#     if counter == 1:
#         print("*")
#     # print("")
# a = int(input())
# b = int(input())
# x = b-a
# if x<0:
#     print("Congratulations, you are within the speed limit!")
# if 0<x<21:
#     print("You are speeding and your fine is $100.")
# elif 20<x<31:
#     print("You are speeding and your fine is $270.")
# elif x>30:
#     print("You are speeding and your fine is $500.")
# for i in range(int(input())):
#     a,b = map(int,input().split())
#     a %=100
#     b %= 100
#
#
#     if a == 17 or b==17:
#         print("NO")
#     elif a%10 == 7:
#         if b == 11:
#             print("YES")
#         else:
#             print("NO")
#     elif b%10 == 7:
#         if a == 11:
#             print("YES")
#         else:
#             print("NO")
#     else:
# #         print("NO")
# def prime_factors(n):
#     factors = []
#
#     while n % 2 == 0:
#         factors.append(2)
#         n = n // 2
#
#
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         while n % i == 0:
#             factors.append(i)
#             n = n // i
#
#     if n > 2:
#         factors.append(n)
#
#     return factors
# n, m = int(input()),int(input())
# adjs = []
# nouns = []
# for i in range(n):
#     adjs.append(input())
# for i in range(m):
#     nouns.append(input())
# for adj in adjs:
#     for noun in nouns:
#         print(f'{adj} as {noun}')
# import math
# def factors(n):
#     facs = set()
#
#     for i in range(1,int(math.sqrt(n))+1):
#         if n % i == 0:
#             facs.add(i)
#             facs.add(n//i)
#     # print(facs)
#     return len(facs)
# counter = 0
# a,b = int(input()),int(input())
# for j in range(a,b+1):
#     if factors(j) == 4:
#         counter+=1
# print(f'The number of RSA numbers between {a} and {b} is {counter}')
all = [[0,461,431,420,0],[0,100,57,70,0],[0,130,160,118,0],[0,167,266,75,0]]
# burger = [0,461,431,420,0]
# side = [0,100,57,70,0]
# drink = [0,130,160,118]
# des = [0,167,266,75,0]
# counter = 0
# # for i in range(4):
# #     counter += all[i][int(input())]
# # print(f'Your total Calorie count is {counter}.')
# # h = int(input())
# # half_h = int((h+1)/2)
# # counter = 1
# # # print(half_h)
# # for iter in range(half_h):
# #
# #     spaces = h*2 - counter*2
# #     for i in range(counter):
# #         print("*",end="")
# #     for i in range(spaces):
# #         print(" ",end="")
# #     for i in range(counter):
# #         print("*",end="")
# #     counter+=2
# #     print("")
# # counter -=2
# # while counter >= 1:
# #     # print(counter)
# #     counter = counter - 2
# #     spaces = h*2 - counter*2
# #
# #     for i in range(counter):
# #         print("*", end="")
# #     for i in range(spaces):
# #         print(" ", end="")
# #     if counter>=3:
# #         for i in range(counter):
# #             print("*", end="")
# #         print("")
# #     if counter == 1:
# #         print("*")
# #     # print("")
# import turtle
#
# # Setup the screen
# screen = turtle.Screen()
# screen.bgcolor("white")
#
# # Create the turtle
# pikachu = turtle.Turtle()
# pikachu.speed(5)
#
# # Function to draw Pikachu's body parts
# def draw_circle(color, radius, x, y):
#     pikachu.penup()
#     pikachu.goto(x, y)
#     pikachu.pendown()
#     pikachu.fillcolor(color)
#     pikachu.begin_fill()
#     pikachu.circle(radius)
#     pikachu.end_fill()
#
# # Draw Pikachu's head
# def draw_head():
#     draw_circle("yellow", 100, 0, -100)
#
# # Draw Pikachu's ears
# def draw_ears():
#     # Left ear
#     pikachu.penup()
#     pikachu.goto(-70, 50)
#     pikachu.setheading(120)
#     pikachu.pendown()
#     pikachu.fillcolor("yellow")
#     pikachu.begin_fill()
#     pikachu.circle(50, 180)
#     pikachu.left(120)
#     pikachu.circle(50, 180)
#     pikachu.end_fill()
#
#     # Tip of the left ear
#     pikachu.fillcolor("black")
#     pikachu.begin_fill()
#     pikachu.circle(50, 60)
#     pikachu.end_fill()
#
#     # Right ear
#     pikachu.penup()
#     pikachu.goto(70, 50)
#     pikachu.setheading(60)
#     pikachu.pendown()
#     pikachu.fillcolor("yellow")
#     pikachu.begin_fill()
#     pikachu.circle(-50, 180)
#     pikachu.right(120)
#     pikachu.circle(-50, 180)
#     pikachu.end_fill()
#
#     # Tip of the right ear
#     pikachu.fillcolor("black")
#     pikachu.begin_fill()
#     pikachu.circle(-50, 60)
#     pikachu.end_fill()
#
# # Draw Pikachu's eyes
# def draw_eyes():
#     # Left eye
#     draw_circle("black", 15, -35, 10)
#     draw_circle("white", 6, -30, 20)  # Shine on left eye
#     # Right eye
#     draw_circle("black", 15, 35, 10)
#     draw_circle("white", 6, 40, 20)   # Shine on right eye
#
# # Draw Pikachu's cheeks
# def draw_cheeks():
#     # Left cheek
#     draw_circle("red", 20, -65, -20)
#     # Right cheek
#     draw_circle("red", 20, 65, -20)
#
# # Draw Pikachu's mouth
# def draw_mouth():
#     pikachu.penup()
#     pikachu.goto(-20, -60)
#     pikachu.setheading(-60)
#     pikachu.pendown()
#     pikachu.circle(20, 120)  # Small curve for smile
#
# # Draw Pikachu's nose
# def draw_nose():
#     draw_circle("black", 5, 0, 0)
#
# # Drawing Pikachu
# draw_head()        # Head
# draw_ears()        # Ears
# draw_eyes()        # Eyes
# draw_cheeks()      # Cheeks
# draw_mouth()       # Mouth
# draw_nose()        # Nose
#
# # Hide the turtle
# pikachu.hideturtle()
#
# # Keep the window open
# turtle.done()
# def hi(a):
#    a*a
# hi(1)
# print(hi(1))
#
# e2dedzd2/fdf = 2
# print(223)
# print = 'print'
# print(print)
# dic = {1:100,2:200}
# print(list(dic.keys())[0])
# #
# def count_odd(lst):
#     i = 0
#     counter = 0
#     while i<len(lst):
#         if lst[i] % 2 != 0:
#             counter+=1
#         i+=1
#     return counter
# print(count_odd([5,-3,2,1,0,11,200,201]))
#
# word = {"dogs":1,"cats":2,"I":3,"socks":4}
# def get_misspelled(line, word_dict):
#     all_words = line.split()
#     results = set()
#     for i in all_words:
#         if i not in word.keys():
#             results.add(i)
#
#     return sorted(results)
# print(get_misspelled("I like socks and I like gloves", word))
a = 0
if a:
    print(1)
