import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        students = load_students(input_file)
        save_students(output_file, students)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


def load_students(input_file):
    students = []
    with open(input_file, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                last, first = [name.strip() for name in row["name"].split(",")]
                house = row["house"]
                students.append({
                    "first": first,
                    "last": last,
                    "house": house
                })
            except (KeyError, ValueError):
                continue
    return students


def save_students(output_file, students):
    fieldnames = ["first", "last", "house"]
    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow(student)


if __name__ == "__main__":
    main()
