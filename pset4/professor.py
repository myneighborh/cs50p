import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        first_num = generate_integer(level)
        second_num = generate_integer(level)
        problem = f"{first_num} + {second_num} = "
        answer = first_num + second_num
        tries = 0

        while tries < 3:
            try:
                guess = int(input(problem))
                if guess == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1
        if tries == 3:
            print(f"{problem}{answer}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
