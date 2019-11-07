# 传递任意数量的参数


def make_pizza(*toppings):
    """打印顾客所有的配料"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print('\t- ' + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
