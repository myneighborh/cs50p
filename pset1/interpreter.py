def main():
    expression = input("Expression: ").strip()
    x, y, z = expression.split(' ')
    result = calculate(x, y, z)
    print(f"{result:.1f}")


def calculate(x, y, z):
    x = int(x)
    z = int(z)

    match y:
        case '+':
            return float(x + z)
        case '-':
            return float(x - z)
        case '*':
            return float(x * z)
        case '/':
            return float(x / z)


if __name__ == "__main__":
    main()
