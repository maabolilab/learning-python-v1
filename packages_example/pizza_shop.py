import random

from tax_calculator import calculate_discount, calculate_gst

print("Hello Sir/Madam")
name = input("What is your name: ")
print()
print(f"Hello {name}, what would you like to order: ")
print("*"* 100)
print("Veggi Pizza")
print("Mozrella Pizza")
print("Farmhouse Pizza")
print("Delecious Pizza")
print("*"* 100)

selected_pizza = input()

pizza_prices = random.randint(200, 500)
pizza_discount = random.randint(15, 25)

final_pizza_price = (pizza_prices - calculate_discount(pizza_prices, pizza_discount))
final_pizza_price_gst = calculate_gst(final_pizza_price)

print()
print("*"* 100)
print(f"You selected: {selected_pizza}₹")
print(f"Pizza Price: {pizza_prices}₹")
print(f"Pizza Discount: {pizza_discount}%")
print(f"Pizza price after discount: {final_pizza_price}₹")
print(f"5% GST: {(final_pizza_price_gst - final_pizza_price):.2}₹")
print(f"Total: {final_pizza_price_gst}₹")
print("*"* 100)