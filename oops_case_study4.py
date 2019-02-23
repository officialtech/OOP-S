class Book:
    print(10 * "*", "Enter Book Details", 10 * "*")

    def details(self):
        self.title = input("Book Title\n").title().strip()
        self.author = input("Book Author\n").title().strip()
        self.quantity = int(input("Quantity of Books\n"))
        self.price = float(input("Price Of One Book\n"))
        self.price *= self.quantity

    def display(self):
        print("{0} is Written by {1} and you have {2} Book/s and Price of Book/s is {3}".format(self.title, self.author,
                                                                                                self.quantity,
                                                                                                self.price))


b = Book()
b.details()
b.display()