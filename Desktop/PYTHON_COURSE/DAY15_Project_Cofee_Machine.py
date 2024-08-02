
from DAY15_PROJECT_COFEEMACHINE_MENU import MENU,resources
profit=0
def is_resource_sufficient(order_ingredients):
  """Return True when order can be made,False if ingredients are insufficient"""  
  for item in order_ingredients:
    if order_ingredients[item]>resources[item] :
        print(f"Sorrry there is not enough {item}")
        return False
  return True
 
#penny=0.01 dollar, nickle=0.05 dollar, dime=0.10 dollar, quarter=0.25 dollar
def process_coins():
    """Returns the total calculated from coins inserted"""
    print("please insert coins")
    total=int(input("how many quarters?:"))*0.25 #to convert it into dollars
    total +=int(input("how many dimes?:"))*0.1
    total +=int(input("how many nickel?:"))*0.05
    total +=int(input("how many pennies?:"))*0.01
    return total

def is_Transaction_successful(money_recieved, drink_cost):
    """Return True when the payment is accepted or False if money is insufficient"""
    if money_recieved>=drink_cost:
        change =round(money_recieved-drink_cost,2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough Money.Money refunded")
        return False
    
def make_coffe(drink_name, order_ingredients):
    """Deduct the required ingredients from resources"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ☕.Enjoy")   
    
    
is_on=True
while is_on:
    choice=input("What would you like espresso/latte/cappuccino:")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}ml")
        print(f"Money:${profit}")
    else :
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
          payment=process_coins()
          if is_Transaction_successful(payment, drink["cost"]):
            make_coffe(choice, drink["ingredients"])
        
