import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    m = re.search(r'src="https?://(www\.)?youtube\.com/embed/([\w-]+)"', s)
    if m:
        return f"https://youtu.be/{m.group(2)}"
    return None

if __name__ == "__main__":
    main()