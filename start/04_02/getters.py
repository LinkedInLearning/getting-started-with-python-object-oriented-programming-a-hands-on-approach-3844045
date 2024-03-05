class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance


# Example usage
if __name__ == "__main__":
    # Create an account
    my_account = BankAccount(account_number="123456789",
                             account_holder="Fred Bloggs", balance=1000.0)

    print("Account Number:", my_account.account_number)
    print("Account Holder:", my_account.account_holder)
    print("Balance:", my_account.balance)
