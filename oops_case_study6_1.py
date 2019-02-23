class Customer:
    print("Welcome to Yatra.com")
    total = 0
    def show(self):
        self.name = input("Name of the Person\n")
        self.accompany = int(input("Number of person\n"))
        self.package = input("Package category (D/H/P)\n").lower()
        self.date = input("Date of Journey\n")

        if self.package == 'd':
            Customer.total = 8000 * self.accompany

        elif self.package == 'h':
            Customer.total = 6000 * self.accompany

        elif self.package == 'p':
            Customer.total = 4000 * self.accompany

    def display(self):
        print(25*"*")
        print("Name ", self.name)
        print("Total no of accompanying ", self.accompany)
        print("Package name ", self.package)
        print("Date of Journey ", self.date)
        print(25*"*")
        print("Total Price For", self.accompany, "People is", Customer.total)


c = Customer()
c.show()
c.display()
