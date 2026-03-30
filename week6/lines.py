import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        counter = 0
        with open(sys.argv[1]) as f:
            for line in f:
                if line.strip() == "" or line.lstrip().startswith("#"):
                    continue
                counter += 1
        print(counter)

    except FileNotFoundError:
        sys.exit("File does not exist")




