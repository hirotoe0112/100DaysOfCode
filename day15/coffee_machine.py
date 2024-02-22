from data import MENU, COIN, resources

current_resources = resources
profit = 0
power_on = True


def off():
    global power_on
    power_on = False
    print("Goodbye.")


def report():
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    print(f"Money: ${round(profit, 2)}")


def check_ingredients(coffee_type):
    required_ingredients = MENU[coffee_type]["ingredients"]
    for ingredient in required_ingredients:
        if current_resources[ingredient] < required_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins(coffee_type):
    total_dollars = int(input("How many quarters?: ")) * COIN["quarters"]
    total_dollars += int(input("How many dimes?: ")) * COIN["dimes"]
    total_dollars += int(input("How many nickles?: ")) * COIN["nickles"]
    total_dollars += int(input("How many pennies?: ")) * COIN["pennies"]
    if total_dollars < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if total_dollars > MENU[coffee_type]["cost"]:
        change = round(total_dollars - MENU[coffee_type]["cost"], 2)
        print(f"Here is ${change} in change.")
    global profit
    profit += MENU[coffee_type]["cost"]
    return True


def make_coffee(coffee_type):
    if check_ingredients(coffee_type) and process_coins(coffee_type):
        required_ingredients = MENU[coffee_type]["ingredients"]
        current_resources["water"] -= required_ingredients["water"]
        current_resources["milk"] -= required_ingredients.get("milk", 0)
        current_resources["coffee"] -= required_ingredients["coffee"]
        print(f"Here is your {coffee_type}. Enjoy!")


def espresso():
    make_coffee("espresso")


def latte():
    make_coffee("latte")


def cappuccino():
    make_coffee("cappuccino")


operations = {
    "off": off,
    "report": report,
    "espresso": espresso,
    "latte": latte,
    "cappuccino": cappuccino,
}


def serve():
    operation = input("What would you like? (espresso/latte/cappuccino): ")
    while operation not in operations:
        print("Invalid operation")
        operation = input("What would you like? (espresso/latte/cappuccino): ")
    operations[operation]()


while power_on:
    serve()
