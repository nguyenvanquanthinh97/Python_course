from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def start():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    coffee_machine(menu, coffee_maker, money_machine)


def coffee_machine(menu, coffee_maker, money_machine):

    drink = get_user_chosen(menu, coffee_maker)

    if not is_able_to_make_drink(coffee_maker, drink):
        return coffee_machine(menu, coffee_maker, money_machine)

    transaction(money_machine, drink)
    coffee_maker.make_coffee(drink)
    return coffee_machine(menu, coffee_maker, money_machine)
    

def get_user_chosen(menu, coffee_maker):
    user_choosen = input(f"What would you like? ({menu.get_items()})")
    found_drink = menu.find_drink(user_choosen)
    if user_choosen == 'off':
        return turn_off_machine()
    if user_choosen == 'report':
        return print_report(coffee_maker)
    if not found_drink:
        return get_user_chosen()
    return found_drink


def turn_off_machine():
    return exit()


def print_report(coffee_maker):
    return coffee_maker.report()


def is_able_to_make_drink(coffee_maker, drink):
    is_resource_sufficient = coffee_maker.is_resource_sufficient(drink)
    if not is_resource_sufficient:
        return False
    return True


def transaction(money_machine, drink):
    if not money_machine.make_payment(drink.cost):
        return transaction(money_machine, drink)
    money_machine.report()
    return True


start()