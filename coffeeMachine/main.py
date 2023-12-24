from coffeeMachineData import MENU, resources

#TODO: Crete user logic to check the MENU with the resources
def checkResources(userChoice):
    water = MENU[userChoice]['ingredients']['water']
    coffee = MENU[userChoice]['ingredients']['coffee']
    cost = MENU[userChoice]['cost']

    if userChoice == 'espresso':
        if water <= resources['water'] and coffee <= resources['coffee']:
            processCoins(userChoice)
        else:
            print('Not enough')
    elif userChoice == 'cappuccino' or userChoice == 'latte':
        milk = MENU[userChoice]['ingredients']['milk']
        if water <= resources['water'] and milk <= resources['milk'] and coffee <= resources['coffee']:
            processCoins(userChoice)
        else:
            print('Not enough')

#TODO: Process coins
def processCoins(userChoice):
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    cost = MENU[userChoice]['cost']
    print('Your cost is:', cost)

    cashQuarters = float(input("Quarters(0.25): ")) * quarters
    cashDimes = float(input("Dimes(0.10): ")) * dimes
    cashNickles = float(input("Nickles(0.05): ")) * dimes
    cashPennies = float(input("Pennies(0.01): ")) * pennies
    summCurrencies = cashQuarters + cashDimes + cashNickles + cashPennies
    print(f'Money paid: {round(summCurrencies,2)}')
    if summCurrencies < cost:
        print("Sorry that's not enough money. Money refunded.")
        userOrder()
    else:
        refund = summCurrencies - cost
        resources['money'] += cost
        print(f"Here is {round(refund,2)} in change.\nCash register: {resources['money']}")
        print(f'Here is your {userChoice} ☕️. Enjoy!')
        userDrinkOrder(userChoice)

#TODO: Process order
def userDrinkOrder(userChoice):
    water = MENU[userChoice]['ingredients']['water']
    coffee = MENU[userChoice]['ingredients']['coffee']
    cost = MENU[userChoice]['cost']

    if userChoice == 'latte' or 'cappuccino':
        milk = MENU[userChoice]['ingredients']['milk']
        waterSum = resources['water'] - water
        coffeeSum = resources['coffee'] - coffee
        resources['water'] = waterSum
        resources['coffee'] = coffeeSum
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
    elif userChoice == 'espresso':
        waterSum = resources['water'] - water
        coffeeSum = resources['coffee'] - coffee
        resources['water'] = waterSum
        resources['coffee'] = coffeeSum
        print(f"Water: {resources['water']}\nCoffee: {resources['coffee']}")

#TODO: ask user to choice an order
def userOrder():
    while True:
        userChoice = input("What would you like? (espresso/latte/cappuccino, off | report): ")
        if userChoice == 'off':
            print('See you.')
            break
        elif userChoice == 'report':
            for i in resources:
                print(i, resources[i])
        else:
            checkResources(userChoice)
userOrder()

