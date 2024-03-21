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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

# TODO: print resources left
def checkReport():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${money}")

# TODO: turn off machine
def turnOff():
    sys.exit()

# TODO: check resources sufficient
def resourceCheck(coffeeType):
    enoughResource = True
    for resource in resources:
        if resources[resource] < menu[coffeeType]["ingredients"][resource]:
            print(f"Sorry there is not enough {resource}.")
            enoughResource = False
    return enoughResource    
    

# TODO: process coins

# TODO: chcek transaction successful


# TODO: main game

