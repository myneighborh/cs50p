import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file_name = sys.argv[1]
    if not file_name.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        scourgify(file_name, sys.argv[2])
    except FileNotFoundError:
        sys.exit(f"Could not read {file_name}")


def scourgify(before, after):
    students = []
    with open(before, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                last, first = [x.strip() for x in row["name"].split(",")]
                house = row["house"]
                students.append({"first": first,
                                "last": last,
                                "house": house})
            except (KeyError, ValueError):
                continue

    with open(after, "w", newline="") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)


if __name__ == "__main__":
    main()
