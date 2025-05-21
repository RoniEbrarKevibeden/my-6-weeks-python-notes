# DICTIONARY - Interactive Menu Order with Total Price

menu = {
    "pizza": 55,
    "burger": 35,
    "pasta": 40,
    "salad": 25
}

order_list = []
total = 0

print("Welcome to the menu!")
print("Available items:")
for item, price in menu.items():
    print(f"- {item.capitalize()}: ${price}")

print("\nType 'done' when you finish ordering.\n")

while True:
    item = input("What would you like to order? ").lower()

    if item == "done":
        break
    elif item in menu:
        order_list.append(item)
        total += menu[item]
        print(f"{item.capitalize()} added to your order. Current total: ${total}")
    else:
        print(f"Sorry, we don't have {item}. Please choose from the menu.")

# Final order summary
print("\nYour order summary:")
for ordered_item in order_list:
    print(f"- {ordered_item.capitalize()} : ${menu[ordered_item]}")

print(f"Total amount to pay: ${total}")
