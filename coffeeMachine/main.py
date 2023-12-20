from coffeeMachineData import MENU, resources

#TODO: Crete user logic to check the MENU with the resources
def checkResources(userChoice):
    water = MENU[userChoice]['ingredients']['water']
    coffee = MENU[userChoice]['ingredients']['coffee']

    cost = MENU[userChoice]['cost']

    if userChoice == 'espresso':
        if water <= resources['water'] and coffee <= resources['coffee']:
            waterSum = resources['water'] - water
            coffeeSum = resources['coffee'] - coffee
            resources['water'] = waterSum
            resources['coffee'] = coffeeSum
            print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
        else:
            print('Not enough')
    elif userChoice == 'cappuccino' or userChoice == 'latte':
        milk = MENU[userChoice]['ingredients']['milk']
        if water <= resources['water'] and milk <= resources['milk'] and coffee <= resources['coffee']:
            waterSum = resources['water'] - water
            milkSum = resources['milk'] - milk
            coffeeSum = resources['coffee'] - coffee
            resources['water'] = waterSum
            resources['milk'] = milkSum
            resources['coffee'] = coffeeSum
            print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}")
        else:
            print('Not enough')

#TODO: Process coins

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
            #print(MENU[userChoice])
            checkResources(userChoice)

userOrder()


# for key, value in resources.items():
#     if value.startswith('bo'):
#         print(key, value)


