class User:

    def __init__(self, first_name, last_name, email, wallet, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.wallet = wallet
        self.id = id

    def get_full_name_string(self):
        """ Returns the user whole name via string concatenation"""
        return f"{self.first_name} {self.last_name}"

    def charge_wallet(self, amount):
        print(self.wallet)
        """ Charges the user's wallet by the given amount """
        self.wallet -= amount

    def add_to_wallet(self, amount):
        """ Add to the users wallet the give amount """ 
        self.wallet += amount 

    def can_afford(self, amount):
        if self.wallet - amount >= 0:
            return True
        else:
            return False  
    