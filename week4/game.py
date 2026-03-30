import random

while True:
    try:
        l = int(input("Level: "))
        if l > 0:
            break
    except ValueError:
        pass

x = random.randint(1, l)

while True:
    try:
        a = int(input("Guess: "))
        if a < x:
            print("Too small!")
        elif a > x:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass

