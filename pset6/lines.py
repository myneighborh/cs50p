import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        lines = count_lines(sys.argv[1])
        print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")


def count_lines(file_name):
    count = 0
    with open(file_name, "r") as file:
        for row in file:
            line = row.strip()
            if line.startswith("#") or line == "":
                continue
            count += 1
    return count


if __name__ == "__main__":
    main()
