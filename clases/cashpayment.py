class CashPayment:

    def __init__(self, amount, cash_received):
        self.amount = amount
        self.cash_received = cash_received

    def process_payment(self):

        if(self.cash_received >= self.amount):

            change = self.cash_received - self.amount

            return f"Payment approved. Change: {change}"

        else:
            return "Insufficient money"