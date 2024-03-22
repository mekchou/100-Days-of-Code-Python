import sys

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


# TODO: promt ask what would you like?
def initialPrompt():
    prompt = input("What would you like? (espresso/latte/cappuccino): ")
    return prompt

# TODO: print resources left
def checkReport(resources, money):
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${money}")

# TODO: turn off machine
# def turnOff():
#     sys.exit()

# TODO: check resources sufficient
def resourceCheck(coffeeType, resources):
    enoughResource = True
    for resource in menu[coffeeType]["ingredients"]:
        if resources[resource] < menu[coffeeType]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}.")
            enoughResource = False
    return enoughResource    
    

# TODO: process coins
def processCoins():
    coins = {
    "quarters": 0,
    "dimes": 0,
    "nickles": 0,
    "pennies": 0
    }   
    for coin in coins:
        coins[coin] = int(input(f"How many {coin}?: "))
    totalCoins = 0.25 * coins["quarters"] + 0.1 * coins["dimes"] + 0.05 * coins["nickles"] + 0.01 * coins["pennies"]
    return totalCoins

# TODO: chcek transaction successful
def checkTransaction(coffeeType, totalCoins):
    if totalCoins == menu[coffeeType]["cost"]:
        return True
    elif totalCoins > menu[coffeeType]["cost"]:
        change = round(totalCoins - menu[coffeeType]["cost"], 2)
        print(f"Here is $ {change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: make coffee
def makeCoffee(coffeeType, resources, money):
    for resource in menu[coffeeType]["ingredients"]:
        resources[resource] -= menu[coffeeType]["ingredients"][resource]
    money += menu[coffeeType]["cost"]
    print(f"Here's your {coffeeType}. Enjoy!")
    return (resources, money)


# TODO: main function
def coffeeMachine():
    resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    }
    money = 0
    
    machineOn = True
    # keep running until machine off
    while machineOn:
        coffee = initialPrompt().lower()
        # turn off
        if coffee == "off":
            machineOn = False
            break
        # show report
        elif coffee == "report":
            checkReport(resources, money)
        # if not in menu, prompt again
        elif coffee in menu:
            if resourceCheck(coffee, resources):
                totalCoins = processCoins()
                if checkTransaction(coffee, totalCoins):
                    (resources, money) = makeCoffee(coffee, resources, money)
                else:
                    break
            # else:
            #     break
            
        
            
coffeeMachine()