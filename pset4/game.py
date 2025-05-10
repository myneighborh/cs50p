import random


def main():
    correct_num = set_level()

    while True:
        guess_num = guess_number()
        if guess_num < correct_num:
            print("Too small!")
        elif guess_num > correct_num:
            print("Too large!")
        else:
            print("Just right!")
            break


def set_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return random.randint(1, level)
        except ValueError:
            continue


def guess_number():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            continue


if __name__ == "__main__":
    main()
