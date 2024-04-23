import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()


if len(sys.argv) == 1:
    figlet.setFont(font= random.choice(fonts))

elif len(sys.argv) == 3:
    if not (sys.argv[1] == "-f" or sys.argv[1] == "--font") or not sys.argv[2] in fonts:
        sys.exit("Invalid usage")
    figlet.setFont(font= sys.argv[2])

print(figlet.renderText(input("Input: ")))