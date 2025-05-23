import csv
import sys

from tabulate import tabulate


def main():
    length = len(sys.argv)
    if length < 2:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]
    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        table = tabulate_table(file_name)
        print(table)
    except FileNotFoundError:
        sys.exit("File does not exist")


def tabulate_table(file_name):
    with open(file_name, "r", newline="") as file:
        reader = csv.DictReader(file)
        content = [row for row in reader]
        return tabulate(content, headers="keys", tablefmt="grid")


if __name__ == "__main__":
    main()
