instructions = []
counterins = 0
while True:
    counterins+=1
    direction = input()
    instructions.append(direction)
    road = input()
    if road == "SCHOOL":
        break
    instructions.append(road)
while not counterins == 1:
    dtn = "".join(instructions[counterins*2-2:counterins*2-1])
    if dtn  == "L":
        print("Turn RIGHT onto ", end="")
        print("".join(instructions[counterins*2-3:counterins*2-2]),end="")
        print(" street.")
    elif dtn == "R":
        print("Turn LEFT onto ", end="")
        print("".join(instructions[counterins*2-3:counterins*2-2]), end="")
        print(" street.")
    counterins -= 1
print("Turn ", end="")
if "".join(instructions[0:1]) == "R":
    print("LEFT",end="")
elif "".join(instructions[0:1]) == "L":
    print("RIGHT",end="")
print(" into your HOME.")



