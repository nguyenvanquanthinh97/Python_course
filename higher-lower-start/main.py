from random import randint

from art import logo, vs
from game_data import data


def game():
    """Call this function to start higher-lower-game"""
    questions = data
    asked_questions = []
    start_game(questions, asked_questions)


def start_game(formatted_data, asked_questions):
    """Starting to handle game logic"""
    formatted_data = [*formatted_data, *asked_questions]
    asked_questions.clear()
    print(logo)
    is_game_end = False
    current_score = 0
    while not is_game_end:
        options = generate_options(formatted_data, asked_questions, num=2)
        print_options(options)
        choosed_option = input("Who has more followers? Type 'A' or 'B': ")
        if (choosed_option.upper() == 'A'):
            choosed_option = options[0]
        elif (choosed_option.upper() == 'B'):
            choosed_option = options[1]
        is_corrected = check_answer(choosed_option, 'follower_count', options)
        if not is_corrected:
            is_game_end = True
        else:
            current_score += 1
            print("You're right! Current score: {}".format(current_score))

    is_continue = input("Do you want to restart the game? 'Y' or 'N': ")
    if is_continue.upper() == 'Y':
        start_game(formatted_data, asked_questions)


def generate_options(questions, asked_questions, num):
    """Remove a random topic questions and add to asked_questions"""
    options = []
    for freq in range(num + 1):
        options.append(questions.pop(randint(0, len(questions) - 1)))

    asked_questions.extend(options)
    return options


def print_options(options):
    """Print options in the choosed topic"""
    showed_options = []
    for option in options:
        name = option["name"]
        description = option["description"]
        country = option["country"]
        showed_options.append(
            "{}, {}, from {}".format(name, description, country))

    print("Compare A: {}".format(showed_options[0]))
    print(vs)
    print("Against B: {}".format(showed_options[1]))


def check_answer(answer, compared_property, compared_options):
    result = False
    max_option = compared_options[0]
    for option in compared_options:
        if compared_property not in option:
            result = False
            break
        if max_option[compared_property] < option[compared_property]:
            max_option = option

    if answer['name'] == max_option['name']:
        result = True

    return result


game()
