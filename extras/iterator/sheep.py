# Generator
# Iterator
# Yield

def main():
    n = int(input("What's n? "))
    gen = sheep(n)

    while True:
        try:
            s = next(gen)
            print(s)
            s += 1
        except StopIteration:
            break

    # for s in sheep(n):
    #     print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()
