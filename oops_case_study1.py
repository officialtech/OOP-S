class Bank:
    def __init__(self):
        ask = input("\n1. New Account\n2. Existing Account Holder\n")
        if ask == 1:
            pass

    def assign(self):
        self.name = input("Name: ")
        self.account = int(input("Account Number: "))
        self.type = input("Account Type (saving/current/fix): ")
        self.amount = int(input("Amount: "))

    def deposit(self):
        self.deposit_amount = int(input("Amount to deposit: "))
        self.amount += self.deposit_amount
        print(self.deposit_amount, "Deposit sucessfully!")
        print()

    def withdraw(self):
        self.withdraw_amount = int(input("Amount to Withdraw: "))

        if self.amount >= self.withdraw_amount:
            print(self.withdraw_amount, "Amount deducted!!!")
            self.amount -= self.withdraw_amount
            print()

    def balance(self):
        print("Your total balance is", self.amount)


b = Bank()
b.assign()

print("\nPlease select options below")
num = int(input("1. Deposit Amount\n2. Withdraw Amount\n3. Balance""\n"))
if num == 1:
    b.deposit()
    # break

elif num == 2:
    b.withdraw()
    # break

elif num == 3:
    b.balance()
    # break