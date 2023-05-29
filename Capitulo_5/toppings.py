available_toppings = [
    'mushrooms',
    'green peppers',
    'extra cheese',
    'olives',
    'pepperoni'
]

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']


for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping.title()}.")
    else:
        print(f"Sorry, we are out of {requested_topping.title()}.")
print("Finished making your pizza")
