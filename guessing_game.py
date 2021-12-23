import random

MODE = {
    "easy": 10,
    "hard": 5
}


def guessing_games():
    result = generate_result(1, 101)
    print('Result', result)

    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a number between 1 and 100.")

    selected_mode = set_game_mode()

    num_of_attempts = MODE[selected_mode]

    check_answer(result, num_of_attempts)

    is_continue = (input("Pross Y to continue the game: ")).upper() == 'Y'
    if is_continue:
        guessing_games()


def set_game_mode():
    selected_mode = ''
    while not selected_mode in MODE.keys():
        selected_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return selected_mode


def generate_result(start, end):
    return random.randint(start, end)


def check_answer(result, num_of_attempts):
    while num_of_attempts > 0:
        print("You have {} attempts remainging to guess the number".format(
            num_of_attempts))
        guessed_number = int(input("Make a guess: "))

        if guessed_number > result:
            print("Too high")
            num_of_attempts -= 1
        elif guessed_number < result:
            print("Too low")
            num_of_attempts -= 1
        else:
            print("Correct")
            break

    if (num_of_attempts == 0):
        print("You lose")


guessing_games()
