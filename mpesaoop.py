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
       