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
    cost = MENU[userChoice]['cost'] #3.0
    print('Your cost is:', cost)
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    cashQuarters = int(input("Quarters(0.25): ")) * quarters
    cashDimes = int(input("Dimes(0.10): ")) * dimes
    cashNickles = int(input("Nickles(0.05): ")) * dimes
    cashPennies = int(input("Pennies(0.01): ")) * pennies
    x = cashQuarters + cashDimes + cashNickles + cashPennies
    print(f'flow {round(x,2)}')
    if x < cost:
        print("Sorry that's not enough money. Money refunded.")
        userOrder()
    else:
        refund = x - cost
        resources['money'] += cost
        print(f"Custmer refund: {round(refund,2)}, Cash register: {resources['money']}")
        userDrinkOrder(userChoice)

#TODO: Process order
def userDrinkOrder(userChoice):
    water = MENU[userChoice]['ingredients']['water']
    coffee = MENU[userChoice]['ingredients']['coffee']
    cost = MENU[userChoice]['cost']

    if userChoice == 'latte' and 'cappuccino':
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
        print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")

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

