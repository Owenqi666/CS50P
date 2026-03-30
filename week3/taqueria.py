menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00,
}

def main():
    total = 0
    while True:
        try:
            x = input("Item: ").lower().strip()
        except EOFError:
            print()
            break
        if x in menu:
            total += menu[x]
            print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()
