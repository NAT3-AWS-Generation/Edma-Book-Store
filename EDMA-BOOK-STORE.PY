# Initial Data of inventory
menu_items = {
    'food': ['pastries', 'desserts', 'wraps', 'savouries', 'pasta'],
    'drinks': ['Fresh Juice', 'smoothies', 'Coffee', 'matcha', 'energy drink']
}
book_list = ['Game of Thrones', 'Power', 'Lion', 'Emotional Intelligence']

# List to store customer orders
orders = []

# Function to display menu items
def display_menu_and_books():
    print("\n--- Menu ---")
    print("Food Menu:", ", ".join(menu_items['food']))
    print("Drink Menu:", ", ".join(menu_items['drinks']))
    print("Books Available:", ", ".join(book_list))
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

# Main function to run the program
def main():
    while True:
        print("Welcome to EDMA's! What can we get you?")
        print("1. View Menu and Place Order")
        print("2. Quit")
        
        choice = input("Please choose an option (1 or 2): ")

        if choice == "1":
            order_collect()
        elif choice == "2":
            print("Thank you for visiting EDMA's!")
            break
        else:
            print("Invalid option, please try again.\n")

# Run the main function
main()

    
