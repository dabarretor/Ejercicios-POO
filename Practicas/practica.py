class BankAccount:
    Bank_name: str= "Bank python"
    def __init__ (self, owner:str, balance: float=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount
        print(f"Has depositado {amount}. Nuevo saldo: {self.balance}")

    def withdraw(self, amount: float):
        if amount > self.balance:
            print(f"Fondos insuficientes para {self.owner}. Saldo actual: {self.balance}")
        else:
            self.balance -= amount
            print(f"Has retirado {amount}. Nuevo saldo: {self.balance}")

    def transfer(self, other_account:"BankAccount", amount: float):
        if amount > self.balance:
            print(f"Transferencia fallida: {self.owner} no tiene fondos suficientes.")
        else:
            self.balance -= amount
            other_account.balance += amount
            print(f"Transferencia exitosa de {amount} a {other_account.owner}.")
            print(f"El saldo de {self.owner} es {self.balance}")
            self.balance -= amount
        other_account.balance += amount
        print(f"the sald is {self.balance}")
        print(f"the owner of the account is {self.owner}")