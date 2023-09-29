from lib.customer import Customer
import pytest 


def test_provide_customer_name():
    user1 = Customer("Andy Baker", "07900000000")

    assert user1.name == "Andy Baker"
    assert user1.phone_number == "07900000000"


def test_update_customer_name():
    user1 = Customer("Jane Smith", "07900000001")

    user1.update_name("John Smith")

    assert user1.name == "John Smith"
    assert user1.phone_number == "07900000001"


def test_update_customer_number():
    user1 = Customer("Mary Jones", "07900000002")

    user1.update_number("07900000022")

    assert user1.name == "Mary Jones"
    assert user1.phone_number == "07900000022"

def test_view__all_customer_info():
    user1 = Customer("Sarah Jane", "07900000003")
    assert user1.view_all_customer_info() == "Name: Sarah Jane, Phone Number: 07900000003"

def test_view_customer_name():
    user1 = Customer("June Black", "07900000004")
    assert user1.view_customer_name() == "Name: June Black"

def test_view_customer_number():
    user1 = Customer("Phil Collins", "07900000005")
    assert user1.view_customer_number() == "Phone Number: 07900000005"


#EDGE CASES
"""
provide class and no name added 
"""
def test_no_name_provided():
    with pytest.raises(Exception) as e:  
        user1 = Customer("", "07900000006")
        user1.phone_number
    error_message = str(e.value)
    assert error_message == "Please provide a name"

"""
provide class no phone added 
"""

def test_no_number_provided():
    with pytest.raises(Exception) as e:  
        user1 = Customer("Morgan Freeman", "")
        user1.name
    error_message = str(e.value)
    assert error_message == "Please provide a number"


"""
provide class phone length invalid
"""

def test_number_provided_too_short():
    with pytest.raises(Exception) as e:  
        user1 = Customer("Betty White", "0790000000")
        user1.phone_number
    error_message = str(e.value)
    assert error_message == "Phone number too short"

