# LEVEL - I

""" class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def display_car_info(self):
        print (f"Car brand: {self.brand} and color: {self.color}")

car_obj1 = Car("AUDI","black")
car_obj1.display_car_info()

car_obj2 = Car("Ferrari","yellow")
car_obj2.display_car_info()
"""

""" class Book:
    def __init__(self,title,author,year = 0):
        self.title = title
        self.author = author
        self.year = year
    def display_details(self):
        print(f"{self.title} written by {self.author} in the year {self.year}.")

book1 = Book("Thousand Splendid Suns","Khaled",2007)
book1.display_details()

book2 = Book("Palace of Illusions","Chitra Banerjee")
book2.display_details() """

""" class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def grade(self):
        if self.marks < 40:
            print(f"{self.name} failed.")
        else:
            print(f"{self.name} passed.")

student1 = Student("Prajwala",99)
student1.grade()
student1 = Student("xyz",39)
student1.grade() 
"""

""" class Dog:
    species = "Canine" #class attribute
    def __init__(self,name,age):
        self.name = name #instance attribute
        self.age = age #instance attribute
    def display_details(self):
        print(f"Name: {self.name} Age: {self.age} Species: {self.species}")

dog1 = Dog("Tommie",7)
dog1.display_details()
dog2 = Dog("Gannu",1)
dog2.display_details()
print()
print("After changing class attribute:")
print()
Dog.species = "Mammal"
dog1.display_details()
dog2.display_details() """


# LEVEL - II

""" print("Bank Account Simulation")

class Account:
    balance = 0
    def deposit(self,amount):
        self.balance += amount
        print(f"Amount added successfully!")
        print(f"Your current balance: {self.balance}")
    def withdraw(self,amount):
        self.balance -=amount
        print(f"Amount withdrawed successfully!")
        print(f"Your current balance: {self.balance}")
    def check_balance(self):
        print(f"Current balance: {self.balance}")

account = Account()
account.deposit(10000)
print('------------------------------------------------')
account.withdraw(500)
print('------------------------------------------------')
account.withdraw(999)
print('------------------------------------------------')
account.deposit(11)
print('------------------------------------------------')
account.check_balance() """

# Shopping Cart

""" class Cart:
    cart_items = {}
    def add(self,name,price):
        self.cart_items[name] = price
    def remove(self,name):
        if name in self.cart_items:
            self.cart_items.pop(name)
        else:
            print("Invalid Item to remove from the cart")
    def total_amount(self):
        for key,val in self.cart_items.items():
            print(f"{key} : {val}")
        total_val = sum(self.cart_items.values())
        print('----------------------------------')
        print(f"Total Cart Value = {total_val}")
        print('----------------------------------')

cart = Cart()
cart.add("Fossil Round Dial Analog Watch",7800)
cart.add("Instax Mini camera",10000)
cart.total_amount()
print()
cart.remove("Instax Mini camera")
cart.total_amount()
print()
cart.remove("MAC") """

# Employee Bonus Calculator

""" class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def apply_bonus(self,bonus):
        self.salary = self.salary + ((bonus/100) * self.salary)
        print(f"Salary after bonus: {self.salary}")

emp1 = Employee("Prajwala",99999)
emp1.apply_bonus(20) """

# Temperature Converter

class Temperature:
    def __init__(self,temperature,unit):
        self.temperature = temperature
        self.unit = unit

    # Coverting and displaying in fahrenheit
    def celsius_to_fahrenheit(self):
        if self.unit.lower() == "f": #if already temp is in fahrenheit
            return self.temperature
        else:
            return (self.temperature - 32) * 5/9
        
    def display_in_fahreheit(self):
        fahrenheit = self.celsius_to_fahrenheit()
        print(f"{self.temperature}°{self.unit.upper()} = {fahrenheit:.2f}°F")
    
    # Coverting and displaying in celsius
    def fahrenheit_to_celsius(self):
        if self.unit.lower() == "c": #if already temp is in celsius
            return self.temperature
        else:
            return (self.temperature - 32) * 9/5
    def display_in_celsius(self):
        celsius = self.fahrenheit_to_celsius()
        print(f"{self.temperature}°{self.unit.upper()} = {celsius:.2f}°C")
    

tem1 = Temperature(35,"c")
tem1.display_in_celsius()
tem1.display_in_fahreheit()

tem2 = Temperature(98,"F")
tem2.display_in_celsius()
tem2.display_in_fahreheit()