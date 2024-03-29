from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


make_coffee = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while make_coffee:
    choice = input(f"What would you like? ({menu.get_items()}): ")

    if choice == "off":
        make_coffee = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
