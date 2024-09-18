# Defining the Restaurant class
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}.")
        print(f"It serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

# Creating three different instances of the Restaurant class
restaurant1 = Restaurant("Ocean's Delight", "Seafood")
restaurant2 = Restaurant("Pasta Palace", "Italian")
restaurant3 = Restaurant("Sushi World", "Japanese")

# Calling describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()