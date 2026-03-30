import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    m = re.fullmatch(r"(\d+)(?::(\d+))? (AM|PM) to (\d+)(?::(\d+))? (AM|PM)", s)
    if not m:
        raise ValueError

    h1, min1, period1 = m.group(1), m.group(2), m.group(3)
    h2, min2, period2 = m.group(4), m.group(5), m.group(6)

    h1, min1 = to24(h1, min1, period1)
    h2, min2 = to24(h2, min2, period2)

    return f"{h1:02}:{min1:02} to {h2:02}:{min2:02}"

def to24(hour, minute, period):
    hour = int(hour)
    minute = int(minute) if minute else 0

    if not (1 <= hour <= 12):
        raise ValueError
    if not (0 <= minute <= 59):
        raise ValueError

    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return hour, minute

if __name__ == "__main__":
    main()