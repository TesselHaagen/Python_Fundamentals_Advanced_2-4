class BankAccount:
    """
    ....

    Attributes:
     - balance (float)
     - holder (str)
    """
    def __init__(self, balance, holder):
        self.balance = balance
        self.holder = holder
    
    def deposit(self, amount):
        """
        Haalt 'amount' van de balans af
        """
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def info(self):
        return f'This bank account is from {self.holder} and has a balance of {self.balance}'
    

bankaccount = BankAccount(0, 'Tessel')
bankaccount.deposit(100)
print(bankaccount.info())