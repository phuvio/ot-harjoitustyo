class Payment:
    def __init__(self, receipt_name, date, amount, transaction, payer, information):
        self.receipt_name = receipt_name
        self.date = date
        self.sum = amount
        self.transaction = transaction
        self.payer = payer
        self.information = information
