import random
import sys
from pyfiglet import Figlet


figlet = Figlet()
FONT_LIST = figlet.getFonts()


def main():
    if len(sys.argv) == 1:
        random_font()
    elif len(sys.argv) == 3:
        convert_font(sys.argv[1], sys.argv[2])
    else:
        sys.exit(1)

    text = input("Input: ")
    print(figlet.renderText(text))


def random_font():
    font_name = random.choice(FONT_LIST)
    figlet.setFont(font=font_name)


def convert_font(font_command, font_name):
    if font_command not in ("-f", "--font"):
        sys.exit(1)
    elif font_name not in FONT_LIST:
        sys.exit(1)
    else:
        figlet.setFont(font=font_name)


if __name__ == "__main__":
    main()
