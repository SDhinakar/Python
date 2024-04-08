import higher_lower_data
import random


def display_accountinfo(account):   
    name=account_1['name']
    description=account_1['description']
    country=account_1['country']
    print(f"Compare A: {name} Is {description}, From {country}")


account_1=random.choice(higher_lower_data.data)
account_2=random.choice(higher_lower_data.data)

print(f"Compare 1: {display_accountinfo(account_1)}")
print(f"Compare 2: {display_accountinfo(account_2)}")
display_accountinfo(account_1)
display_accountinfo(account_2)