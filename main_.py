from savings_account import SavingsAccount
from checking_account import CheckingAccount


def main_():

    # Savings accounts
    sav1 = SavingsAccount("Momo", 1000, 100, "1111", "9999", 0.05)
    sav2 = SavingsAccount("Ava", 2000, 200, "2222", "8888", 0.03)

    # Checking accounts
    chk1 = CheckingAccount("Ismail", 1500, 100, "3333", "7777", 500)
    chk2 = CheckingAccount("Arwa", 1000, 100, "4444", "6666", 300)
    # Scenario
    chk1.withdraw(400)
    chk1.transfer(300)

    sav1.apply_interest()

    sav1.print_info()
    sav2.print_info()
    chk1.print_info()
    chk2.print_info()


if __name__ == "__main__":
    main_()
