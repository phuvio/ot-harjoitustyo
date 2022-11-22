class Payment:
    def __init__(self, receipt, date, sum, payer, adjustment, information):
        self.receipt = receipt
        self.date = date
        self.sum = sum
        self.payer = payer
        self.adjustment = adjustment
        self.information = information
