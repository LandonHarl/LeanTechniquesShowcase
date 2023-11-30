class ChangeCalculator:
    def __init__(self, amount):
        self.amount = amount
        self.change = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.bills = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]

    def verify_input(self):
        try:
            self.amount = float(self.amount)
            return "Valid option."
        except ValueError:
            return "Invalid option. Please enter a number value. "


    def calc_change(self):
        ctr = 0
        for currency in self.bills:
            count = int(self.amount / currency)
            self.change[ctr] = count
            if count > 0:
                self.amount -= float(currency * count)
                self.amount = round(self.amount, 2)
            ctr += 1

        return self.change

