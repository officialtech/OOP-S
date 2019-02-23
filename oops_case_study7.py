class Furniture:
    price = 0
    def __init__(self):
        print(12*"*","Welcome to the World's of Wood!",12*"*")
        print("\nSelect your requirements\n")
    def category(self):

        print("1. Chair\n2.Stool\n3. Rocking Chair\n4. Bench\n5. Couch\n"
              "6. Chaise Longue\n7. Bed\n8. Waterbed\n9. Headboard\n"
              "10. Sofa Bed\n11. Chess Table\n12. Desk\n"
              "13. Dining Table\n14. Tv Tray Table\n15. Bookcase")
        requirement = int(input())
        if requirement == 1:
            print("Chair!")
            Furniture.price += 19.01
        elif requirement == 2:
            print("Stool!")
            Furniture.price += 15.12
        elif requirement == 3:
            print("Rocking Chair!")
            Furniture.price += 17.19

        elif requirement == 4:
            print("Bench!")
            Furniture.price += 15.12

        elif requirement == 5:
            print("Couch!")
            Furniture.price += 25.01

        elif requirement == 6:
            print("Chaise Longue!")
            Furniture.price += 18.18
        elif requirement == 7:
            print("Bed!")
            Furniture.price += 27.12
        elif requirement == 8:
            print("Water Bed!")
            Furniture.price += 29.19
        elif requirement == 9:
            print("Head Board!")
            Furniture.price += 15.12
        elif requirement == 10:
            print("Sofa Bed!")
            Furniture.price += 17.17
        elif requirement == 11:
            print("Chess Table!")
            Furniture.price += 12.12
        elif requirement == 12:
            print("Desk!")
            Furniture.price += 14.12
        elif requirement == 13:
            print("Dining Table!")
            Furniture.price += 26.01
        elif requirement == 14:
            print("Tv Tray Table!")
            Furniture.price += 15.19
        elif requirement == 15:
            print("Bookcase!")
            Furniture.price += 14.12
        else:
            print("Sorry! we have only above given products...")


Furniture().category()
print("Your Total Price is", Furniture.price)
