# Initial Data of inventory
menu_items = {
    'food': ['pastries', 'desserts', 'wraps', 'savouries', 'pasta'],
    'drinks': ['Fresh Juice', 'smoothies', 'Coffee', 'matcha', 'energy drink']
}
book_list = ['Game of Thrones', 'Power', 'Lion', 'Emotional Intelligence']
specials = []
orders = []

# Function to display menu items
def display_menu_and_books():
    print("\n--- Menu ---")
    print("Food Menu:", ", ".join(menu_items['food']))
    print("Drink Menu:", ", ".join(menu_items['drinks']))
    print("Books Available:", ", ".join(book_list))
    if specials:
        print("Today's Specials:", ", ".join(specials))
    print("\n")

# Function to collect customer orders
def order_collect():
    print("Please choose your items from the following menu.")
    
    # Display the menu
    display_menu_and_books()

    # Collect food choices
    food_choices = input("Enter the food items you'd like to order (comma separated): ").split(',')
    food_choices = [item.strip() for item in food_choices if item.strip() in menu_items['food']]

    # Collect drink choices
    drink_choices = input("Enter the drinks you'd like to order (comma separated): ").split(',')
    drink_choices = [item.strip() for item in drink_choices if item.strip() in menu_items['drinks']]

    # Collect book choices
    book_choices = input("Enter the books you'd like to order (comma separated): ").split(',')
    book_choices = [item.strip() for item in book_choices if item.strip() in book_list]

    # Collect customer details
    customer_name = input("Enter your name: ")
    customer_address = input("Enter your address: ")

    # Store the order
    order = {
        'name': customer_name,
        'address': customer_address,
        'food': food_choices,
        'drinks': drink_choices,
        'books': book_choices
    }

    # Append the order to the orders list
    orders.append(order)

    # Confirmation message
    print("\n--- Order Summary ---")
    print(f"Customer Name: {customer_name}")
    print(f"Food Items: {', '.join(food_choices) if food_choices else 'None'}")
    print(f"Drink Items: {', '.join(drink_choices) if drink_choices else 'None'}")
    print(f"Books Ordered: {', '.join(book_choices) if book_choices else 'None'}")
    print(f"Delivery Address: {customer_address}\n")
    print("Your order has been placed! Thank you.\n")

# Function to update menu
def update_menu():
    print("\n--- Update Menu ---")
    category = input("Do you want to update 'food', 'drinks', or 'books'? ").lower()

    if category == 'food' or category == 'drinks':
        action = input(f"Do you want to 'add' or 'remove' an item from the {category} menu? ").lower()
        item = input(f"Enter the item to {action}: ").strip()

        if action == 'add':
            menu_items[category].append(item)
            print(f"{item} has been added to the {category} menu.")
        elif action == 'remove' and item in menu_items[category]:
            menu_items[category].remove(item)
            print(f"{item} has been removed from the {category} menu.")
        else:
            print("Item not found or invalid action.")
    elif category == 'books':
        action = input("Do you want to 'add' or 'remove' a book? ").lower()
        book = input(f"Enter the book title to {action}: ").strip()

        if action == 'add':
            book_list.append(book)
            print(f"{book} has been added to the book list.")
        elif action == 'remove' and book in book_list:
            book_list.remove(book)
            print(f"{book} has been removed from the book list.")
        else:
            print("Book not found or invalid action.")
    else:
        print("Invalid category.")

# Function to add specials
def add_specials():
    print("\n--- Add Specials ---")
    special = input("Enter the special item you'd like to add: ").strip()
    specials.append(special)
    print(f"{special} has been added to today's specials.")

# Function to view customer details
def view_customer_details():
    if orders:
        print("\n--- Customer Orders ---")
        for i, order in enumerate(orders, 1):
            print(f"Order {i}:")
            print(f"Customer Name: {order['name']}")
            print(f"Delivery Address: {order['address']}")
            print(f"Food Items: {', '.join(order['food']) if order['food'] else 'None'}")
            print(f"Drink Items: {', '.join(order['drinks']) if order['drinks'] else 'None'}")
            print(f"Books Ordered: {', '.join(order['books']) if order['books'] else 'None'}\n")
    else:
        print("No customer orders found.")

# Main function to run the program
def main():
    while True:
        print("\nWelcome to EDMA's! What can we get you?")
        print("1. View Menu and Place Order (Customer)")
        print("2. Update Menu/Books (Employee)")
        print("3. Add Specials (Employee)")
        print("4. View Customer Details (Employee)")
        print("5. Quit")
        
        choice = input("Please choose an option (1-5): ")

        if choice == "1":
            order_collect()
        elif choice == "2":
            update_menu()
        elif choice == "3":
            add_specials()
        elif choice == "4":
            view_customer_details()
        elif choice == "5":
            print("Thank you for visiting EDMA's!")
            break
        else:
            print("Invalid option, please try again.\n")

# Run the main function
main()


    
