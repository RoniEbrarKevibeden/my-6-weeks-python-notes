# Start with a predefined shopping list
shopping_list = []

# Add items to the list
shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")

# Display the list using a loop
print("Your shopping list:")
for item in shopping_list:
    print("-", item)

# Remove an item
shopping_list.remove("bread")

print("\nUpdated list:")
for item in shopping_list:
    print("-", item)

# Reset the list and take user input
shopping_list = []

print("\nEnter items for your shopping list.")
print("Type 'done' when you're finished.\n")

while True:
    item = input("Add item: ")
    if item.lower() == 'done':
        break
    shopping_list.append(item)

# Final list output
print("\nYour final shopping list:")
for product in shopping_list:
    print("-", product)
