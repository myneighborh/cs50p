import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(?:[1-9]\d{0,2}|0)\.(?:[1-9]\d{0,2}|0)\.(?:[1-9]\d{0,2}|0)\.(?:[1-9]\d{0,2}|0)$"
    if re.match(pattern, ip):
        octets = ip.split(".")
        return all(0 <= int(octet) <= 255 for octet in octets)
    return False


if __name__ == "__main__":
    main()
