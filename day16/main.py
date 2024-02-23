from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    operation = input(f"What would you like? ({menu.get_items()}): ")
    if operation == "off":
        print("Goodbye.")
        break
    if operation == "report":
        coffee_maker.report()
        money_machine.report()
        continue
    ordered_drink = menu.find_drink(operation)
    if ordered_drink is None:
        continue
    if coffee_maker.is_resource_sufficient(
        ordered_drink
    ) and money_machine.make_payment(ordered_drink.cost):
        coffee_maker.make_coffee(ordered_drink)
