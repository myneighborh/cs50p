import sys

from PIL import Image, ImageOps


def main():
    # Check number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Validate file extensions
    if not input_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        sys.exit("Invalid input")
    if not output_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        sys.exit("Invalid output")

    # Ensure input and output have the same extension
    if input_file.rsplit('.', 1)[-1].lower() != output_file.rsplit('.', 1)[-1].lower():
        sys.exit("Input and output have different extensions")

    try:
        get_shirt(input_file, output_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def get_shirt(input_file, output_file):
    with Image.open(input_file) as image:
        with Image.open("shirt.png") as shirt:
            # Resize and crop the input image to match the shirt size
            image = ImageOps.fit(image, shirt.size)
            # Overlay the shirt image onto the input image using alpha mask
            image.paste(shirt, shirt)
            image.save(output_file)


if __name__ == "__main__":
    main()
