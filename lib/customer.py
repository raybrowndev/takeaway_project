class Customer:
    def __init__(self, name, phone_number):
            if name == "":
                raise Exception("Please provide a name")
            self.name = name

            if phone_number == "":
                raise Exception("Please provide a number")
            elif len(phone_number) <11:
                raise Exception("Phone number too short")
            self.phone_number = phone_number

    def update_name(self,new_name):
        self.name = new_name

    def update_number(self, new_number):
        self.phone_number = new_number

    def view_all_customer_info(self):
        return f"Name: {self.name}, Phone Number: {self.phone_number}"

    def view_customer_name(self):
        return f"Name: {self.name}"

    def view_customer_number(self):
        return f"Phone Number: {self.phone_number}"
