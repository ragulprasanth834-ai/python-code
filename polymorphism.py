class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__dep = 0
        self.__wit = 0

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount"

        if amount > 100000:
            return "High amount cannot be deposited"

        if self.__balance + amount > 500000:
            return "Balance limit exceeded (500000)"

        self.__balance += amount
        self.__dep += 1
        return f"{amount} deposited successfully"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"

        if self.__balance - amount < 1000:
            return "Minimum balance rule violated"

        self.__balance -= amount
        self.__wit += 1
        return f"Debited {amount}. Current balance: {self.__balance}"

    def get_balance(self):
        return self.__balance

    def transaction_history(self):
        return f"Deposits: {self.__dep}, Withdrawals: {self.__wit}"