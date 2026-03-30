def main():
    while True:
        x = input("Fraction: ")
        result = get_percentage(x)
        if result is not None:
            break
    if result >= 99:
        print("F")
    elif result <= 1:
        print("E")
    else:
        print(f"{result}%")

def get_percentage(x):
    try:
        a, b = x.split("/")
        a = int(a)
        b = int(b)
        if b == 0:
            raise ZeroDivisionError
        if a > b:
            raise ValueError
        return round(a / b * 100)
    except (ValueError, ZeroDivisionError):
        return None

if __name__ == "__main__":
    main()