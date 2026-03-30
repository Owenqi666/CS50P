import pyfiglet
import sys
import random

if len(sys.argv) == 1:
    font = random.choice(pyfiglet.FigletFont.getFonts())
elif len(sys.argv) == 3 and sys.argv[1] == "-f":
    font = sys.argv[2]
else:
    sys.exit("Invalid usage")

x = input("Input: ")

try:
    print(pyfiglet.figlet_format(x, font=font))
except pyfiglet.FontNotFound:
    sys.exit("Invalid usage")