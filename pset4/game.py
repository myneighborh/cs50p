import random


def main():
    # Prompt for a valid level and generate the correct number
    while True:
        try:
            level = get_level()
            correct_num = set_correct_number(level)
            break
        except ValueError:
            continue

    # Keep asking for guesses until the correct number is guessed
    while True:
        try:
            guess_num = get_guess_number()
            if guess_num < correct_num:
                print("Too small!")
            elif guess_num > correct_num:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            continue


def get_level():
    level = int(input("Level: "))
    if level > 0:
        return level
    else:
        raise ValueError


def set_correct_number(level):
    if level <= 0:
        raise ValueError
    return random.randint(1, level)


def get_guess_number():
    guess = int(input("Guess: "))
    if guess > 0:
        return guess
    else:
        raise ValueError


if __name__ == "__main__":
    main()
