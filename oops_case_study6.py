class Customer:
    print("Welcome to Yatra.com")
    #discover_india = 8000
    #holiday_hungama = 6000
    #pilgrimage = 4000

    def show(self):
        self.name = input("Name of the Person\n")
        self.accompany = int(input("Number of person\n"))
        self.package = input("Package category (D/H/P)\n").lower()
        self.date = input("Date of Journey\n")
        self.total = 0
        if self.package == 'd':
            self.total = 8000 * self.accompany

        elif self.package == 'h':
            self.total = 6000 * self.accompany

        elif self.package == 'p':
            self.total = 4000 * self.accompany

    def display(self):
        print(25*"*")
        print("Name ", self.name)
        print("Total no of accompanying ", self.accompany)
        print("Package name ", self.package)
        print("Date of Journey ", self.date)
        print(25*"*")
        print("Total Price For", self.accompany, "People is", self.total)


c = Customer()
c.show()
c.display()
