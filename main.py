#Program Requirements


# TODO 1. print report;

Menu = {
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


coffee_machine = False
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

# TODO 2. Check resources sufficient?
def is_resources_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient [item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO 3. Process coins
# Coins request
def process_coins():
    print("Please insert your coins!")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


# TODO 4. Check transaction successful?
def is_transaction_successful (money_received, drink_cost):
    if money_received >= drink_cost:
        change = round (money_received - drink_cost, 2)
        print(f"Here is your ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False

# TODO 5. Make coffee
def make_coffee (drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

# Function should set up first & while loop put on the back
is_on = True
while is_on:
    cust_choose = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    if cust_choose == "off":
        is_on = False
    elif cust_choose == "report":
        print(f"Water: {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}g.")
        print(f"Money: S{profit}.")
    else:
        drink = Menu[cust_choose]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(cust_choose, drink["ingredients"])



