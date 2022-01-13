from data import MENU, coffee_emoji, resources

# TODO Coins: Penny 0.01, Dime 0.05, Nickel 0.1, Quarter 0.25 cents
# TODO Resources: 300 ml water, 200 ml milk, 100gr coffee
# TODO drinks:  "What would you like? (espresso/latte/cappuccino): "
#               espresso    50  ml water    18 gr coffee                    $1.50
#               latte       200 ml water    24 gr coffee    150 ml milk     $2.50
#               cappuccino  250 ml water    24 gr coffee    100 ml milk     $3.00
# TODO report: prints remaining resources (including money) "Water: 100ml\n.."
# TODO ask for drink order: check if resources are sufficient for selected drink. "Sorry there is not enough water."
# TODO "Please insert coins. How many quarters? ..": check if coins cover cost, and if so,
#  check if change needs to be provided. if needed "Here is $1.14 in change." followed by
#  "Here is your {coffee_emoji} Enjoy!" or "Sorry that's not enough money. Money refunded."

money = 0


def report():
    global resources, money
    for item in resources:
        print(f"{item}: {resources[item]}")
    print(money)

def check_resources(order):
    global resources
    check = True
    for item in resources:
        if item in MENU[order]["ingredients"]:
            if resources[item] < MENU[order]["ingredients"][item]:
                print(f"Sorry there is not enough {item}.")
                check = False
    return check


def make_coffee(order):
    global resources
    for item in resources:
        if item in MENU[order]["ingredients"]:
            resources[item] -= MENU[order]["ingredients"][item]
    print(f"Here is your {coffee_emoji} Enjoy!")


def collect_coins(order):
    global money
    print("Please insert coins. ")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    cents = int(input("How many cents? "))
    total = .25 * quarters + .1 * dimes + .05 * nickels + .01 * cents
    change = total - MENU[order]["cost"]
    if change > 0:
        print(f"Here is ${change} in change.")
        money += total - change
        return True
    elif change == 0:
        money += total
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def validate(order):
    if order == "report":
        report()
    elif order in MENU:
        check = check_resources(order)
        return check
    else:
        print("Please try again.")


def coffee_machine():
    stay_on = True
    while stay_on:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        lets_make_it = validate(order)
        if lets_make_it:
            if collect_coins(order):
                make_coffee(order)



coffee_machine()
