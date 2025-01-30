# homework5_Kathleen_Ashbaker.py

# List Exercise
# Create a list with 6 items
items = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

# Print the items in the list
print("Items in the list:", items)

# Print the first two items using a slice
print("The first two items in the list are:", items[0:2])

# Print the middle two items using a slice
print("The middle two items in the list are:", items[2:4])

# Print the first and last items using indexes
print("The first and last items in the list are:", items[0], items[-1])

# Tuple Exercise
# Tuple containing five basic foods offered by the restaurant
menu = ('pasta', 'pizza', 'salad', 'burger', 'sushi')

# Print each item on the menu using a for loop
print("Original menu:")
for food in menu:
    print(food)

# Update the menu by replacing two of the items
updated_menu = list(menu)
updated_menu[1] = 'sandwich'  # Replacing pizza with sandwich
updated_menu[3] = 'taco'      # Replacing burger with taco
updated_menu = tuple(updated_menu)

# Print each item on the revised menu using a loop
print("Updated menu:")
for food in updated_menu:
    print(food)
