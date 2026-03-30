def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n < 0:
                raise ValueError("必须是正数")
            return n
        except ValueError:
            pass

def main():
    x = get_int("输入正整数: ")
    print(f"你输入了 {x}")

main()