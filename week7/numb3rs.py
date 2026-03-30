import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    m = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    
    if m:
        for i in range(1, 5):
            g = m.group(i)
            if str(int(g)) != g:
                return False
            if not 0 <= int(g) <= 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()