import random


def main():
    # while True:
    #     try:
    #         level = get_level()
    #         break
    #     except ValueError:
    #         continue
    level = get_level()
    score = 0

    # Repeat 10 problems
    for _ in range(10):
        problem, answer = generate_problem(level)
        tries = 0

        # Allow up to 3 attempts per problem
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

        # Show correct answer if user failed 3 times
        if tries == 3:
            print(f"{problem}{answer}")

    # Print final score
    print(f"Score: {score}")


def get_level():
    # level = int(input("Level: "))
    # if level in [1, 2, 3]:
    #     return level
    # else:
    #     raise ValueError

    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


def generate_problem(level):
    x = generate_integer(level)
    y = generate_integer(level)
    problem = f"{x} + {y} = "
    answer = x + y
    return problem, answer


if __name__ == "__main__":
    main()
