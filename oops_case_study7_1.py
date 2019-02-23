class Furniture:

    name = input("Name of the Product: ")  # static variable
    height = float(input("Height in (ft): "))  # static variable
    breadth = float(input("Breadth in (ft): "))  # static variable
    color = input("Colour: ")  # static variable
    material = input("Material: ")   # static variable
    budget = float(input("Budget in $: "))   # static variable
    time = int(input("Time Constraints in (days): "))   # static variable

    def show(self):  # method
        print(15 * "*")
        print("Product Name is", self.name)
        print("Height of", self.name, "is", self.height, "ft.")
        print("Breadth of", self.name, "is", self.breadth, "ft.")
        print("Colour of the", self.name, "is", self.color)
        print("Material will be", self.material)
        print("Budget for", self.name, "is", self.budget, "$")
        print("Expecting Delivary Time", self.time, "days")


f = Furniture()  # creating object and assigning to variable 'f'
f.show()   # calling 'show' method