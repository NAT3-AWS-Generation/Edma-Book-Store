# initial Data of inventory

menu_items = {
    'food': ['pastries', 'desserts', 'wraps', 'savouries', 'pasta'],
    'drinks': ['Fresh Juice', 'smoothies', 'Coffee', 'matcha', 'energy drink'] 
}
book_list = ['Game of Thrones', 'Power', 'lion', 'Emotional intelligence'] 

## customer data functions

def displayMenu_andbooks():
    print("Food Menu:", menu_items['food'])
    print("Drink Menu:", menu_items['drinks'])
    print("Books Availiable:", book_list)

def order_collect():
     print("Choose your food and drink from our food menu")
     food_choices = input().split(',')




