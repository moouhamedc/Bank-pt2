from bank_account import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self, customer_name, balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self,amount):
        if amount > self.transfer_limit:
            print("Transfer limit exceeded")
            return

        if self.current_balance - amount < self.minimum_balance:
            print("Not enough money")
            return

        self.current_balance -= amount
        print("Transfer completed")