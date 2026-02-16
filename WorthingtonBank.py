class Worthington:

    bank_title = "Worthington Bank"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("You don't have enough money to withdraw.")
            return
        self.current_balance -= amount

    def print_customer_information(self):
        print("Bank:", Worthington.bank_title)
        print("Customer:", self.customer_name)
        print("Current Balance:", self.current_balance)
        print("Minimum Balance:", self.minimum_balance)
        print()


momo = Worthington("Momo", 200, 100)
ava = Worthington("Ava", 150, 50)
ismail = Worthington("Ismail", 300, 200)

momo.withdraw(50)
ava.deposit(100)

momo.print_customer_information()
ava.print_customer_information()
ismail.print_customer_information()
