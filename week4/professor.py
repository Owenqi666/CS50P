import random

def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x in [1, 2, 3]:
                return x
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

def main():
    level = get_level()
    mark = 0
    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        counter = 0
        while True:
            try:
                ans = int(input(f"{a} + {b} = "))
                if ans == a + b:
                    mark += 1
                    break
                else:
                    counter += 1
                    if counter == 3:
                        print(f"{a} + {b} = {a + b}")
                        break
                    print("EEE")
            except ValueError:
                print("EEE")
    print(f"Score: {mark}/10")

if __name__ == "__main__":
    main()