import random

from tax_calculator import calculate_discount, calculate_gst

print("Hello Sir/Madam")
name = input("What is your name: ")
print()
print(f"Hello {name}, what would you like to order: ")
print("*"* 100)
print("Aloo Tikki Burger")
print("Panner Tikki Burger")
print("Cheeze Tikki Burger")
print("Salat Tikki Burger")
print("*"* 100)

selected_burger = input()

burger_prices = random.randint(50, 100)
burger_discount = random.randint(10, 20)

final_burger_price = (burger_prices - calculate_discount(burger_prices, burger_discount))
final_burger_price_gst = calculate_gst(final_burger_price)

print()
print("*"* 100)
print(f"You selected: {selected_burger}₹")
print(f"Burger Price: {burger_prices}₹")
print(f"Burger Discount: {burger_discount}%")
print(f"Burger price after discount: {final_burger_price}₹")
print(f"5% GST: {(final_burger_price_gst - final_burger_price):.2}₹")
print(f"Total: {final_burger_price_gst}₹")
print("*"* 100)