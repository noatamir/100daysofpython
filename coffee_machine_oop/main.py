from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

the_maker = CoffeeMaker()
the_money = MoneyMachine()
coffee_menu = Menu()


def coffee_machine():
    stay_on = True
    while stay_on == True:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "off":
            stay_on = False
            break
        elif order == "report":
            the_maker.report()
            the_money.report()
        elif coffee_menu.find_drink(order).name == order:
            coffee = coffee_menu.find_drink(order)
            lets_make_it = the_maker.is_resource_sufficient(coffee)
            if lets_make_it:
                if the_money.process_coins():
                    the_maker.make_coffee(coffee)
        else:
            print("Please try again.")



coffee_machine()