class BankAccount:

    bank_title = "Worthington Bank"

    def __init__(self, customer_name, balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = balance
        self.minimum_balance = minimum_balance

        self._account_number = account_number
        self.__routing_number = routing_number

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("Insufficient funds.")
            return
        self.current_balance -= amount

    def get_account_number(self):
        return self._account_number

    def get_routing_number(self):
        return self.__routing_number

    def print_info(self):
        print()
        print("Bank:", BankAccount.bank_title)
        print("Customer:", self.customer_name)
        print("Balance:", self.current_balance)
        print()
