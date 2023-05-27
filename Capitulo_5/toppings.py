requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print(f"Sorry, we are out of {requested_topping.title()}.")
        else:
            print(f"Adding {requested_topping.title()}.")
print("Finished making your pizza")
