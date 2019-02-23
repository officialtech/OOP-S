class Bank_account:


    def details(self, name, account_no, account_type, balance = 0.0):
        self.name = name
        self.account_no = account_no
        self.account_type = account_type
        self.balance = balance

    def display(self):
        print("Name:", self.name)
        print("Account Number:", self.account_no)
        print("Account Type:", self.account_type)
        print("Balance Amount:", self.balance)

b = Bank_account()
b.details('jb', 1001010, 'Saving', 1010)
b.display()