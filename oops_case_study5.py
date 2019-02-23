class Person:
    def __init__(self):
        print("Please Enter your details\n")

    def person(self):
        self.first = input("First Name\n")
        self.last = input("Last Name\n")
        self.email = input("Email Address\n")
        self.dob = input("Date Of Birth\n")
        print("Your name is ", self.first, self.last, "\nYour Email Address is",self.email, "\nYour Birth Date is", self.dob)



p = Person()
p.person()
