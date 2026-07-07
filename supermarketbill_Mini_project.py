                        ### Super market bill system ##

products = {
    "Rice" : 60,
    "Sugar": 45,
    "Milk" : 30,
    "Bread": 40,
    "Eggs" : 6,
    "Oil" : 120,
    "Soap" :35,
    "Biscuits":25
}

cart = {}

Store_name ="Feresh supermarket"
locaction_name ="Nandyal,India"
print("=" * 50)
print(f"\tWelcome to {Store_name}")
print(f"\tLocation: {locaction_name}")
print("=" * 50)

customer_name = input("Enter customer name: ").title()
print("\nAvailable Products")
print("-" * 50)
print(f"{'Product':<20}{'Price':>10}")
print("-" * 50)

for item,price in products.items():
    print(f"{item:<20}₹{price:>8}")
print("-" * 50)

while True:
    products_name = input( "\nEnter product name to buy (or type 'exit' to finish): ").title()
    if products_name.lower() =="exit":
        break
    if products_name not in products:
        print("Product not available! Please choose from the list.")
        continue
    quantity = input(f"Enter quantity for {products_name}: ")
    if not quantity .isdigit():
        print("Invalid quantity! Please enter numbers only.")
        continue
    quantity = int(quantity)

    if products_name in cart:
        cart[products_name] += quantity
    else:
         cart[products_name] = quantity

    print(f"{products_name} added to cart successfully!")

    print("\n")
print("=" * 60)
print(f"{Store_name:^60}")
print(f"{locaction_name:^60}")
print("=" * 60)

print(f"Customer Name : {customer_name}")
print("-" * 60)

print(f"{'Item':<15}{'Qty':<10}{'Price':<10}{'Total':<10}")
print("-" * 60)

total_amount = 0

for item,quantity in cart.items():
    price =products[item]
    item_total = price*quantity
    total_amount += item_total
    print(f"{item:<15}{quantity:<10}{price:<10}₹{item_total:<10}")

print("-" * 60)

tax = total_amount * 0.12
final_amount = total_amount + tax

print(f"{'Subtotal':<40}₹{total_amount:.2f}")
print(f"{'Tax (12%)':<40}₹{tax:.2f}")
print(f"{'Grand Total':<40}₹{final_amount:.2f}")

print("=" * 60)
print("Thank You for Shopping With Us!")
print("Visit Again 😊")
print("=" * 60)




