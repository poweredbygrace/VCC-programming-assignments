
# ///////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////

# 2) A shopping cart has a list of items priced as follows: 
# prices = [ 10.5, 11.4, 16, 27, 25, 16.7, 44.5 ]. 
# In the shopping card, the number corresponding items are as follows: 
# counts = [ 2, 3, 1, 1, 2, 2, 1].
  
# Write a function that does the followings in the same order it is requested bellow:
#   a) compute the total cost of the shopping card and print as message like this:
#   "The total cost of your shopping card is ...."
  
#   b) Next, compute the average price of the items (means totalCost / number_of_all_items) and print it with appropriate message:
#   "average item price is ..." .
  

def shoppingfunciton():
    prices = [10.5, 11.4, 16, 27, 25, 16.7, 44.5]
    counts = [2, 3, 1, 1, 2, 2, 1]
    ind_costs = [0]
    ind_counts = [0]

    for i in range(len(prices)):
        ind_item_cost = prices[i]*counts[i]
        total = ind_item_cost + ind_costs[-1]
        ind_costs[0] = total


        total_counts = counts[i] + ind_counts[-1]
        ind_counts[0] = total_counts


        # print(f'{ind_item_cost} + {ind_costs[-1]} = {total}')

    print(f'The total cost of your shopping cart is {ind_costs[0]}')
    print(f'The average price of your shopping cart is {round(ind_costs[0]/ind_counts[0], 2)}')
    # ind_costs

shoppingfunciton()
