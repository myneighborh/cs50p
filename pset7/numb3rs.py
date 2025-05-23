import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    octet = r"(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)"
    pattern = rf"^{octet}\.{octet}\.{octet}\.{octet}$"
    return bool(re.fullmatch(pattern, ip))


if __name__ == "__main__":
    main()
