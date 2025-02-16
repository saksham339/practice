# Hotel menu
menu = {
    "pizza": 40,
    "pasta": 50,
    "burger": 60,
    "salad": 70,
    "coffee": 80
}
print(menu)

# Greet
print("Welcome to Restaurant!")
print("pizza: Rs40\npasta: Rs50\nburger: Rs60\nsalad: Rs70\ncoffee: Rs80")

order_total = 0

while True:
    item = input("Enter the name of the item you want to order: ").lower()  # Convert input to lowercase
    if item in menu:
        order_total += menu[item]
        print(f"Your item {item} has been added to your order.")
    else:
        print(f"Order item {item} is not available yet!")

    another_order = input("Do you want to order another item? (yes/no): ").lower()
    if another_order != "yes":
        break  # Exit the loop if the user doesn't want to order more items

print(f"The total amount to pay is Rs{order_total}")
