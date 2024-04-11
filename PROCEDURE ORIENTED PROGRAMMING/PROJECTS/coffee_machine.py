Menu={
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
    },
    "cost":200,
    },"expresso":{
        "ingredients":{
            "water":100,
            "milk":0,
            "coffee":24,
    },"cost":100,
    },"cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
    },"cost":250,
    }
}
profit=0
resources= {
    "water":500,
    "milk":200,
    "coffee":100,
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("Please insert coins")
    total=0
    coins_five=int(input("How many 5 cents coins? "))
    coins_ten=int(input("How many 10 cents coins? "))
    coins_twenty=int(input("How many 20 cents coins? "))
    total=coins_five*5+coins_ten*10+coins_twenty*20
    return total

def is_payment_successful(money_received,coffee_cost):
    if money_received>=coffee_cost:
        global profit
        profit+=coffee_cost
        change=money_received-coffee_cost
        print(f"Here is Rs{change} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(coffee_type,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {coffee_type}. Enjoy!")


is_on=True
while is_on:
    chioce=input("what would you like to have? (latte/expresso/cappuccino): ")
    if chioce=="off":
        is_on=False
    elif chioce=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        coffee_type=Menu[chioce]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment=process_coins()
            if is_payment_successful(payment,coffee_type['cost']):
                make_coffee(chioce,coffee_type['ingredients'])