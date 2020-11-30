class Transaction:

    def __init__(self, user, date, time, merchant, amount, tag, id = None):
        self.user = user
        self.date = date
        self.time = time
        self.merchant = merchant
        self.amount = format(amount, '.2f')
        self.tag = tag
        self.id = id



    