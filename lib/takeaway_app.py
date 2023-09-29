class TakeawayApp:
    def __init__(self, restaurant_manager):
        self.restaurant_manager = restaurant_manager
    
    def list_all_restaurants(self):
        return self.restaurant_manager.show_all_restaurants()

    def select_restaurant(self, name):
        return self.restaurant_manager.select_restaurant_by_name(name)

    def select_restaurant_by_name():
        pass
