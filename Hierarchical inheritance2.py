'''Develop an online shopping cart system. Define a base class Product
with attributes like name, price, and methods for adding to the cart.
Create derived classes for different product types (electronics, clothing)
and use polymorphism for handling the cart.'''
class Product:
    def get_details(self):
        self.id=input("Enter product id:")
        self.name=input("Enter product name:")
        self.price=float(input("Enter price:"))
       
    def add_to_cart(self):
        print(self.name,"added to cart.")
       
    def display(self):
        print("Product id:",self.id)
        print("Product name:",self.name)
        print("Price:",self.price)

class Electronics(Product):
    def get_electronics_details(self):
        super().get_details()
        super().add_to_cart()
        self.brand = input("Enter brand:")
        self.warranty = input("Enter warranty:")

    def display(self):
        super().display()
        print("Brand:",self.brand)
        print("Warranty:",self.warranty)

class Clothing(Product):
    def get_cloth_details(self):
        super().get_details()
        super().add_to_cart()
        self.size = input("Enter cloth size:")
        self.color = input("Enter cloth color:")
       
    def display(self):
        super().display()
        print("Size:",self.size)
        print("Color:",self.color)

while True:
    print("\n1.Electronics\n2.Clothing\n3.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        e=Electronics()
        e.get_electronics_details()
        print("\n----Electronics details----")
        e.display()
        print("-"*25)
    elif ch==2:
        c=Clothing()
        c.get_cloth_details()
        print("\n----Clothing details----")
        c.display()
        print("-"*25)
    elif ch==3:
        print("\nExiting.......")
        break
    else:
        print("Invalid input")
