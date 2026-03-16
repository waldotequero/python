class MpesaAccount:
    def __init__(self, name, phone, balance):
        self.name = name
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited",amount)
        print("your balance is",self.balance)
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}")
            print(f"New balance is {self.balance}")
        else:
            print("Insufficient balance")
    def check_balance(self):
        print(f" Balance is {self.balance}")

user1 = MpesaAccount("Waldo", 254712345678, 1000)
user1.check_balance() 
user1.deposit(500)
user1.check_balance()
user1.withdraw(20000)

user2 = MpesaAccount("Alice", 254798765432, 2000)
user2.check_balance()
user2.deposit(1000)
user2.check_balance()
user2.withdraw(500)

user3 = MpesaAccount("Bob", 254701234567, 1500)
user3.check_balance()
user3.deposit(200)
user3.check_balance()
user3.withdraw(300)

user4 = MpesaAccount("Charlie", 254712345679, 500)
user4.check_balance()
user4.deposit(300)
user4.check_balance()
user4.withdraw(100)

user5 = MpesaAccount("David", 254798765433, 2500)
user5.check_balance()
user5.deposit(500)
user5.check_balance()
user5.withdraw(1000)

from abc import ABC, abstractmethod
# ENCAPSULATION
class MpesaAccount:
    def __init__(self,name,balance):
    self.name=name
    self.__balance=balance #private variable
    def deposit(self,amount):
        self.__balance+=amount
        print(f"Deposited {amount}.  Balance {self.__balance}")
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrawn {amount}. New balance is {self.__balance}")
            return True
        return False
        
        
    def GetBalance(self):
        return self.__balance
    # ABSTRACTION
class MpesaService(ABC):
    @abstractmethod
    def access_service(self,account,amount):
        pass
    @abstractmethod
    def buy_airtime(self,amount):
        pass

    # SEND MONEY
class SendMoney(MpesaService):
    def access_service(self,account,amount):
        if account.withdraw(amount):
            print(f"Sent {amount} to another user.")
        else:
            print("Transaction failed. Insufficient balance.")
    
    # LIPA NA MPESA
class LipaNaMpesa(MpesaService):
    def access_service(self,account,amount):
        if account.withdraw(amount):
            print(f"Paid {amount} to a merchant using Lipa na Mpesa.")
        else:
            print("Payment failed. Insufficient balance.")
    
    # FULIZA
class Fuliza(MpesaService):
    def __init__(self,limit):
        self.limit=limit
    def access_service(self,account,amount):
        balance=account.GetBalance()
        if amount<=balance:
            account.withdraw(amount)
            print("Transaction completed without Fuliza.")
        elif amount<=balance+self.limit:
            overdraft=amount-balance
            account.withdraw(balance)
            print(f"Transaction completed using Fuliza overdraft of {overdraft}.")
        else:
            print("Transaction exceeds Fuliza limit.")

      # M-SHWARI SAVINGS

class Mshwari(MpesaService):
    def __init__(self,savings):
      self.savings=0       
    def access_service(self,account,amount):
        if account.withdraw(amount):
            self.savings+=amount
            print(f"Saved {amount} to M-Shwari. Total savings: {self.savings}")
        else:
            print("Not enough balance to save.")  

# LOANS
class Loan(MpesaService):
    def __init__(self,limit):
        self.limit=limit
        self.loan_balance=0
    def access_service(self,account,amount):
        if amount<=self.limit:
            account.deposit(amount)
            self.loan_balance+=amount
            print(f"Loan of {amount} approved. Total loan: {self.loan_balance}")
        else:
            print("Loan request exceeds limit.")

   # MAIN PROGRAM
account=MpesaAccount("WALDO",500)
send_money=SendMoney()
lipa=LipaNaMpesa()
fuliza=Fuliza(1000)
mshwari=Mshwari()
loan=Loan(1000)

print("Initial balance:",account.GetBalance())
#save to M-Shwari
mshwari.access_service(account,200)
# send money
send_money.access_service(account,100)
#pay merchant
lipa.access_service(account,150)
# use Fuliza
fuliza.access_service(account,400)
# take loan
loan.access_service(account,500)
print("Final balance:",account.GetBalance())

