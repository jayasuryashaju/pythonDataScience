"""
Bank

account creating

deposit

withdraw

message


"""

class Bank:
    bank_name = 'State Bank of India'
    account_number = 10000000000

    def message(self, amount=0, debit=False, credit=False, account=False):
        if debit:
            print(amount, "has been debited from your account \n current balance : ", self.account_balance, "\n")

        elif credit:
            print(amount, "has been credited from your account \n current balance : ", self.account_balance, "\n")

        elif account:
            print("Hai, ", self.fname + " " + self.lname, " your account with account number", self.account_number,
                  "has been created successfully.", "\n Your current balance is : ", self.account_balance, "\n")

    def account_create(self, fname, lname, age, phone_number):
        self.fname = fname
        self.lname = lname
        self.bank_name = Bank.bank_name
        self.age = age
        self.account_number = Bank.account_number + 1
        self.phone_number = phone_number
        self.min_balance = 3000
        self.account_balance = self.min_balance

        self.message(account=True)

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            self.message(amount, debit=True)
        else:
            print("insufficient balance \n")

    def deposit(self, amount):
        self.account_balance += amount

        self.message(amount, credit=True)


obj1 = Bank()

obj1.account_create('vinu', 'r', 24, 8330840185)
obj1.deposit(400)
obj1.withdraw(389999)
obj1.withdraw(1500)

print(obj1.fname, obj1.lname, obj1.account_number, obj1.account_balance, obj1.bank_name)
