class Car:
    # constructor
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        # method

    def drive(self):
        print(f"{self.brand} is my dream Car, I love the color {self.color}.")

# create object
car1 = Car("Mercedes", "Black")  
car1.drive()
car2 = Car("BMW", "White")
car2.drive()
car3 = Car("Audi", "Red")
car3.drive()
car4 = Car("Toyota", "Blue")
car4.drive()
car5 = Car("Honda", "Silver")
car5.drive()
car6=Car("shelby cobra","golden")
car6.drive()
              
class Shoes:   
    #constructor
    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size
    #method
    def wear(self):
        print(f"{self.brand} shoes are my favorite, I love the color {self.color} and size {self.size}.")
    # create object
shoe1=Shoes("nike","white",8)
shoe1.wear()
shoe2=Shoes("adidas","black",9)
shoe2.wear()
shoe3=Shoes ("puma","red",7)
shoe3.wear()
shoe4=Shoes("reebok","blue",10)
shoe4.wear()
shoe5=Shoes("converse","green",6)
shoe5.wear()


class Fruits:
    #constructor
    def __init__(self, color, type, price):
        self.color = color
        self.type = type
        self.price = price
    #method
    def display(self):
        print(f"{self.type} is a delicious fruit, it is {self.color} in color and costs Ksh{self.price:}.")
    # create object
fruit1 = Fruits("yellow", "banana", 1.50)
fruit1.display  ()
fruit2 = Fruits("red", "apple", 2.00)
fruit2.display()
fruit3 = Fruits("orange", "orange", 1.75)
fruit3.display()
fruit4 = Fruits("green", "grape", 3.00)
fruit4.display()
fruit5 = Fruits("purple", "plum", 2.50)
fruit5.display()
