
def OrderCoffee(weight):
    coffee_price_per_pound = 10.50
    shipping_cost_per_pound = 0.86
    overhead_cost = 1.50

    # Calculate total cost
    coffee_cost = coffee_price_per_pound * weight
    shipping_cost = shipping_cost_per_pound * weight
    total_cost = coffee_cost + shipping_cost + overhead_cost
    print(f"The total cost for {weight} pounds of coffee is ${total_cost:.2f}.")

    return total_cost


order1 = OrderCoffee(2)
order2 = OrderCoffee(5)
order3 = OrderCoffee(10)

