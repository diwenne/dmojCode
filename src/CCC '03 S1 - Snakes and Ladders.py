counter = 1
while True:

    roll = int(input())
    if roll == 0:
        print("You Quit!")
        break
    elif counter + roll == 100:
        print("You are now on square", str(counter+roll))
        print("You Win!")
        break
    elif counter+roll > 100:
        print("You are now on square", counter)
    else:
        counter += roll
        if counter == 9:
            counter = 34
        elif counter == 40:
            counter = 64
        elif counter == 67:
            counter = 86
        elif counter == 99:
            counter = 77
        elif counter == 90:
            counter = 48
        elif counter == 54:
            counter = 19
        print("You are now on square", str(counter))