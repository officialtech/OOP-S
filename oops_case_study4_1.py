class Book_details:
    counter = 0
    price = 0

    def __init__(self):
        print("Welcome to the book store!")
        print()

    def kid(self):
        print(10 * "*", "Welcome to Kid's Books", 10 * "*")
        print()
        self.kid_select = int(input(
            "1. Wipe Clean Giant Activity Workbook\n2. On The Come Up-Book 2\n3. Journey to New Berk\n4. Five Feet Apart\n5. Meet the New Dragons\n"))
        if self.kid_select == 1:
            print("Wipe Clean Giant Activity Workbook is Added!")
            Book_details.counter += 1
            Book_details.price += 11.97

        elif self.kid_select == 2:
            print("On the come up-Book 2 is Selected!")
            Book_details.counter += 1
            Book_details.price += 15.19

        elif self.kid_select == 3:
            print("Journey to New Berk is Selected!")
            Book_details.counter += 1
            Book_details.price += 4.99

        elif self.kid_select == 4:
            print("Five Feet Apart is Added!")
            Book_details.counter += 1
            Book_details.price += 12.91

        elif self.kid_select == 5:
            print("Meet The New Dragon is Selected!")
            Book_details.counter += 1
            Book_details.price += 6.99

    def bio_auto(self):
        print(10 * "*", "Welcome to Biography & Autobiography Books", 10 * "*")
        print()
        self.bio_select = int(input(
            "1. Target Club Pick Aug 2013\n2. Becoming 2\n3. Whiskey in a Teacup\n4. Born a Crime\n5. Upside: A Memory\n"))
        if self.bio_select == 1:
            print("Target Club Pick Aug 2013 is Added!")
            Book_details.counter += 1
            Book_details.price += 22.75

        elif self.bio_select == 2:
            print("Becoming is Selected!")
            Book_details.counter += 1
            Book_details.price += 13.59

        elif self.bio_select == 3:
            print("Whiskey in a Teacup is Selected!")
            Book_details.counter += 1
            Book_details.price += 24.50

        elif self.bio_select == 4:
            print("Born a Crime is Added!")
            Book_details.counter += 1
            Book_details.price += 19.60

        elif self.bio_select == 5:
            print("The Upside: A Memory is Selected!")
            Book_details.counter += 1
            Book_details.price += 12.75
        else:
            print("Sorry!")

    def cook_food_wine(self):
        print("Welcome to Cooking, Food and Wine Books!")
        print()
        self.cfw_select = int(input(
            "1. Forks Over Knives\n2. Plenty\n3. Healthy Smoothie\n4. Cannabis Cocktails,Mocktails & Tonics\n5. Complete Beer Course\n"))
        if self.cfw_select == 1:
            print("Forks Over Knives is added!")
            Book_details.counter += 1
            Book_details.price += 9.79

        elif self.cfw_select == 2:
            print("Plenty is selected!")
            Book_details.counter += 1
            Book_details.price += 21.99

        elif self.cfw_select == 3:
            print("Healthy Smoothie Added!")
            Book_details.counter += 1
            Book_details.price += 11.14

        elif self.cfw_select == 4:
            print("Cannabis Cocktails,Mocktails & Tonics is Selected!")
            Book_details.counter += 1
            Book_details.price += 15.63

        elif self.cfw_select == 5:
            print("Complete Beer Course is Added!")
            Book_details.counter += 1
            Book_details.price += 21.20
        else:
            print("Sorry!")

    def fiction_literature(self):
        print("Welcome to Action & Thiriller World!")
        print()
        print(
            "1. The outsider\n2. Every Breath\n3. Forgotten Girls\n4. Empty Bottles\n5. The sweetest Thing\n6. Black Leopard Red Wolf\n")
        self.fiction = int(input())
        if self.fiction == 1:
            print("Here Your 'The Outsider Book'")
            Book_details.counter += 1
            Book_details.price += 17.56

        elif self.fiction == 2:
            print("Every Breath Nice choice!")
            Book_details.counter += 1
            Book_details.price += 19.16

        elif self.fiction == 3:
            print("'Here it\'s FORGOTTEN GIRLS!'")
            Book_details.counter += 1
            Book_details.price += 12.56

        elif self.fiction == 4:
            print("'Empty Bottles' is Ready!")
            Book_details.counter += 1
            Book_details.price += 19.50

        elif self.fiction == 5:
            print("'The Sweetest Thing' NICE CHOICE! Great")
            Book_details.counter += 1
            Book_details.price += 13.56

        elif self.fiction == 6:
            print("Here 'BLACK LEOPARD RED WOLF'")
            Book_details.counter += 1
            Book_details.price += 21.16
        else:
            print("We are unable to Give you", self.fiction)

    def religion(self):
        print("Hello! Welcome to The Purity World")
        print()
        print("1. Girl, Wash Your Face\n2. It's Not Supposed to Be This Way\n3. Weekly Prayer Project\n")
        religion = int(input())
        if self.religion == 1:
            print("'Girl, Wash Your Face' is ready")
            Book_details.counter += 1
            Book_details.price += 16.19

        elif self.religion == 2:
            print("'It\'s Not Supposed to Be This Way' is ready to out")
            Book_details.counter += 1
            Book_details.price += 16.19

        elif self.religion == 3:
            print("'The Weekly Project' is ready")
            Book_details.counter += 1
            Book_details.price += 11.89
        else:
            print("Sorry for", self.religion)

    def self_improvement(self):
        print("Welcome Human's Humanity")
        print()
        print("1. You are a BADASS\n2. You are a BADASS at Making Money\n3. Odd 1s Out\n")
        self.improve = int(input())
        if self.improve == 1:
            print("'You are a BADASS' Book Ready")
            Book_details.counter += 1
            Book_details.price += 9.19

        elif self.improve == 3:
            print("'You are a BADASS at Making Money'")
            Book_details.counter += 1
            Book_details.price += 12.80

        elif self.improve == 2:
            print("'Odd 1s Out'")
            Book_details.counter += 1
            Book_details.price += 11.00
        else:
            print(self.improve, "isn't available!")

    def teen(self):
        print("Wao! This is a Teen World!")
        print()
        print("1. P.S. I Still Love You\n2. The Hate U Give\n3. Always and Forever\n4. On The Come Up\n")
        _teen_ = int(input())
        if self._teen_ == 1:
            print("'P.S. I Still Love You' Book Selected")
            Book_details.counter += 1
            Book_details.price += 8.79

        elif self._teen_ == 2:
            print("'THE HATE YOU GIVE' Book Selected!")
            Book_details.counter += 1
            Book_details.price += 15.19

        elif self._teen_ == 4:
            print("'ON THE COME UP' Book Selected")
            Book_details.counter += 1
            Book_details.price += 15.19

        elif self._teen_ == 3:
            print("'Always And Forever' Book Ready")
            Book_details.counter += 1
            Book_details.price += 8.79
        else:
            print("It's so sorry to say that we haven't", self._teen_)

    # def others(self):


book = Book_details()
print(10 * "*", "Select your choice", 10 * "*")
print()
print(
    "1. Kid's Book\n2. Biography & Autobiography\n3. Cooking, Food and Wine\n4. Fiction & Literature\n5. Religion\n6. Self-improvement\n7. Teen's Books\n8. Others\n")
select = int(input())

if select == 1:
    book.kid()

elif select == 2:
    book.bio_auto()

elif select == 3:
    book.cook_food_wine()

elif select == 4:
    book.fiction_literature()

elif select == 5:
    book.religion()

elif select == 6:
    book.self_improvement()

elif select == 7:
    book.teen()

# elif select == 8:
# book.others()

else:
    print("Sorry we don't have", select)

print("Total Bill: ", Book_details.price)