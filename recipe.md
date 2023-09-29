# Solo Project - TAKEAWAY


## 1. Describe the Problem

 <!-- INCOMPLETE -->
> As a customer  
> So that I can check if I want to order something  
> I would like to see a list of dishes with prices.

 <!-- INCOMPLETE -->
> As a customer  
> So that I can order the meal I want  
> I would like to be able to select some number of several available dishes.
 <!-- INCOMPLETE -->
> As a customer  
> So that I can verify that my order is correct  
> I would like to see an itemised receipt with a grand total

Use the `twilio-python` package to implement this next one. You will need to use
mocks too.
 <!-- INCOMPLETE -->
> As a customer  
> So that I am reassured that my order will be delivered on time  
> I would like to receive a text such as "Thank you! Your order was placed and
> will be delivered before 18:52" after I have ordered.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

+-------------------------------------+
|           Takeaway App             |
+-------------------------------------+
| - restaurant_manager: RestaurantManager |
| - customer: Customer               |
| - order: Order                     |
| - twilio_integration: TwilioIntegration |
+-------------------------------------+
| + view_all_restaurants(): List[str]|
| + select_restaurant(name: str)
|       select restaurnt from string by letter: A = restraunt 1, B = restaurant 2 etc.        
| + view_menu(): List[MenuItem]      |
| + add_to_basket(item: MenuItem)    |
| + view_basket(): List[MenuItem]    |
| + remove_from_basket(item: MenuItem)|
| + view_total_cost(): float         |
| + view_customer_info(): Tuple[str, str]|
| + update_customer_info(name: str, phone: str)|
| + view_order_summary(): str        |
| + complete_order(): str            |
| + send_confirmation_message(phone: str)|
+-------------------------------------+

+-------------------------------------+
|       RestaurantManager            |
+-------------------------------------+
| - restaurants: List[Restaurant]    |
+-------------------------------------+
| + view_all_restaurants(): List[str]|
| + select_restaurant(name: str)     |
        return: selected restaurant 
+-------------------------------------+

+-------------------------------------+
|           Customer                 |
+-------------------------------------+
| - name: str                        |
| - phone: str                       |
+-------------------------------------+
| + take_customer_info(name: str, phone: str)|
| + view_customer_info(): Tuple[str, str]|
| + update_customer_info(name: str, phone: str)|
+-------------------------------------+

+-------------------------------------+
|           Order                     |
+-------------------------------------+
| - basket: List[MenuItem]           |
+-------------------------------------+
| + add_to_basket(item: MenuItem)    |
| + view_basket(): List[MenuItem]    |
| + remove_from_basket(item: MenuItem)|
| + view_total_cost(): float         |
| + view_order_summary(): str        |
| + complete_order(): str            |
+-------------------------------------+

+-------------------------------------+
|     TwilioIntegration              |
+-------------------------------------+
|  - (Twilio integration details)     |
+-------------------------------------+
| + send_confirmation_message(phone: str)|
+-------------------------------------+



## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

def test_provide_customer_name():
    pass


def test_update_customer_name():
    pass

def test_view__all_customer_info():
    pass

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._




