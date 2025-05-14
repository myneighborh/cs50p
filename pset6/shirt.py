import sys

from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    before = sys.argv[1]
    after = sys.argv[2]
    if not before.lower().endswith(('.jpg', '.jpeg', '.png')):
        sys.exit("Invalid input")
    if not after.lower().endswith(('.jpg', '.jpeg', '.png')):
        sys.exit("Invalid output")

    if before.rsplit('.', 1)[-1].lower() != after.rsplit('.', 1)[-1].lower():
        sys.exit("Input and output have different extensions")

    try:
        get_shirt(before, after)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def get_shirt(before, after):
    with Image.open(before) as image:
        with Image.open("shirt.png") as shirt:
            image = ImageOps.fit(image, shirt.size)
            image.paste(shirt, shirt)
            image.save(after)


if __name__ == "__main__":
    main()
