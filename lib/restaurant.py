#menu for each restaurant
class Restaurant:
    def __init__(self):
        self.restaurants = {
            "Pac Donalds": {"menu list": [{"Burger": 30, "PAC Nuggets": 20, "Sad Meal": 10}]},
            "9 Guys": {"menu list": [{"Burger": 1, "Fries": 2, "Milkshake": 3}]},
            "Grub Way": {"menu list": [{"Sandwich (S)": 100, "Sandwich (L)": 200, "Cookies": 50}]},
            "Moonbucks": {"menu list": [{"Coffee": 1.5, "Hot Chocolate": 2.6, "Cakes": 3.8}]}
        }

    def show_all_restaurants(self):
        return list(self.restaurants.keys())

    def select_restaurant_by_name(self, search_name):
        return self.restaurants.get(search_name)


