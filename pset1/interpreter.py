def main():
    expression = input("Expression: ")
    x, y, z = expression.split(' ')
    result = calculate(x, y, z)
    if isinstance(result, str):
        print(result)
    else:
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
            try:
                return float(x / z)
            except ZeroDivisionError:
                return "Error"


if __name__ == "__main__":
    main()
