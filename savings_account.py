from bank_account import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, customer_name, balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, balance, minimum_balance, account_number, routing_number)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
