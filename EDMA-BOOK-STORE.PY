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
<<<<<<< HEAD
    
=======


def order_collect():
     print("Choose your food and drink from our food menu")
     food_choices = input().split(',')

def main():
    while True:
        print("Welcome to Edma's book store!")
        print("1. View menu and place order")
        print("2. Quit")

        user_choice = input("Select option 1 or 2: ")
        if user_choice == "2":
            break
        elif user_choice == "1":
            display_menu_and_books()

main()
>>>>>>> debfe9721e108941133823835373bbb718750ff7
