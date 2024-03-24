class CashRegister:
    def __init__(self):
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, item_name, price, quantity=1):
        if quantity <= 0:
            return "Invalid quantity value"
        for _ in range(quantity):
            self.items.append(item_name)
            self.total += price
            self.last_transaction_amount = price
        return self.total

    def void_last_transaction(self):
        if self.last_transaction_amount != 0:
            self.total -= self.last_transaction_amount
            self.last_transaction_amount = 0
            return self.total
        else:
            return "No transaction to void"

    def apply_discount(self, discount):
        if discount > 0 and discount <= 100:
            discount_amount = self.total * discount / 100
            self.total -= discount_amount
            return self.total
        else:
            return "Invalid discount value"
