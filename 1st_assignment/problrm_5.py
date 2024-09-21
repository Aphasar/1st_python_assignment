'''Problem 5: Grocery List Tracker
You are managing a grocery store inventory. Write a program that asks the user to input the name
and price of 5 items and store them in a list. Then, display the total cost of all items.'''



prices = []    #Initialize an empty list
for i in range(5):             # Ask the user to input the price
    price = float(input(f"Enter the price of item {i + 1}: "))
    prices.append(price)         # Add the price to the list
    
total_cost = sum(prices)       #total cost
print(f"\nTotal cost of all items: ${total_cost:.2f}")
