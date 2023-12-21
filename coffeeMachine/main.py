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
            processCoins(userChoice)
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
            print(f"Remaining resources:\nWater: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']} \nMoney: {resources['money']}")
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

    #cashRegister = int(input("Please insert coins:\n(quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01)"))
    cashQuarters = int(input("Quarters(0.25): ")) * quarters
    cashDimes = int(input("Dimes(0.10): ")) * dimes
    cashNickles = int(input("Nickles(0.05): ")) * dimes
    cashPennies = int(input("Pennies(0.01): ")) * pennies
    x = cashQuarters + cashDimes + cashNickles + cashPennies
    print(f'flow {x}')
    #  = 10 * 0.25 = 2.5
    #  = 2.5 - 3.0 = 0.5
    #new_cost = x - cost
    if x < cost:
        print("Sorry that's not enough money. Money refunded.")
        userOrder()
    else:
        refund = x - cost
        resources['money']  += cost
        print(f"Custmer refund: {round(refund,2)}, Cash register: {resources['money']}")

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
        # elif userChoice == 'espresso' or 'latte' or 'cappuccino':
        #     processCoins(userChoice)
        #     checkResources(userChoice)
        else:
            #print(MENU[userChoice])
            checkResources(userChoice)



userOrder()


# for key, value in resources.items():
#     if value.startswith('bo'):
#         print(key, value)


