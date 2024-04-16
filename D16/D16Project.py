import sys
sys.path.append(r'V:\100-Days-of-Code-Python\module')

from coffeeMachine_coffee_maker import CoffeeMaker
from coffeeMachine_money_machine import MoneyMachine
from coffeeMachine_menu import MenuItem
from coffeeMachine_menu import Menu


# TODO: main function
def coffeeMachine():
    moneyMachine = MoneyMachine()
    coffeeMaker = CoffeeMaker()
    menu = Menu()
    # menuItem = MenuItem()
    machineOn = True
    # keep running until machine off
    while machineOn:
        options = menu.get_items()
        choice = input(f"What would you like? ({options})")
        # turn off
        if choice == "off":
            machineOn = False
            break
        # show report
        elif choice == "report":
            coffeeMaker.report()
            moneyMachine.report()
        # if not in menu, prompt again
        else :
            drink = menu.find_drink(choice)
            if drink != None:
                if coffeeMaker.is_resource_sufficient(drink):
                    if moneyMachine.make_payment(drink.cost):
                        coffeeMaker.make_coffee(drink)
                    # else:
                        # break
                # else:
                #     break
            
        
            
coffeeMachine()
# print(make_payment())
# print(Menu().find_drink("latte").name)
# mm.MoneyMachine().make_payment(0.5)
# print(Menu().find_drink("latte").name)
# menu = Menu().get_items()
# print(menu)