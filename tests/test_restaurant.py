from lib.restaurant import Restaurant

def test_return_all_restaurants():
    all = Restaurant()
    result = all.show_all_restaurants()
    assert result == ['Pac Donalds', '9 Guys', 'Grub Way', 'Moonbucks']


def test_select_restaurant_by_name_return_menu():
    selection = Restaurant()
    result = selection.select_restaurant_by_name("9 Guys")
    assert result == {"menu list": [{"Burger": 1, "Fries": 2, "Milkshake": 3}]}
