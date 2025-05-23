import random
import sys

from pyfiglet import Figlet


figlet = Figlet()
FONT_LIST = figlet.getFonts()


def main():
    try:
        if len(sys.argv) == 1:
            font_name = random_font()
        elif len(sys.argv) == 3:
            font_name = selected_font(sys.argv[1], sys.argv[2])
        else:
            raise ValueError("Invalid usage")

        text = input("Input: ")
        figlet.setFont(font=font_name)
        print(figlet.renderText(text))

    except ValueError:
        sys.exit("Invalid usage")


def random_font():
    return random.choice(FONT_LIST)


def selected_font(font_command, font_name):
    if font_command not in ("-f", "--font"):
        raise ValueError("Invalid usage")
    elif font_name not in FONT_LIST:
        raise ValueError("Invalid usage")
    return font_name


if __name__ == "__main__":
    main()
