# Input practice
# Michael Coleman

item_name = input("Enter item Name: ")
item_price = int(input("Enter item price:"))
state_base_tax = 7.25
local_tax = 3.0
sales_tax = local_tax + state_base_tax
final_price = item_price + (item_price * sales_tax / 100)

print(f"Item Name: {item_name}")
print()
print(f"Subtotal: ${item_price:.2f}")
print(f"Sales Tax: {sales_tax:.2f}%")
print(f"Final Price: ${final_price:.2f}")

