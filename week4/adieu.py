import inflect

def main():
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            print()
            break

    p = inflect.engine()
    print("Adieu, adieu, to", p.join(names))

if __name__ == "__main__":
    main()
