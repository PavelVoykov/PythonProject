import re
bill = 0
class Product:
    def __init__(self, name):
        self.name = name

class Vegetable(Product):
    def __init__(self, name, price, cal):
        self.cal = cal
        self.price = price
        super().__init__(name)
    def Price(self):
        global bill
        bill += self.price
        print(self.name)
        print(bill)

class Meat(Product):
    def __init__(self, name, price, cal):
        self.cal = cal
        self.price = price
        super().__init__(name)
    def Price(self):
        global bill
        bill += self.price
        print(self.name)
        print(bill)
def AddProducts():
    
    name = input('This product is called:\n')
    price = input('The price of this product is:\n')
    cal = input('How many calories countains this product?\n')
    
    number = input('Enter 8 digit number')
    
    f = open('EveryProduct.txt', 'a')
    f.write('{} '.format(name))
    fwrite('{} '.format(price))
    f.write('{} '.format(cal))
    f.write('#{}\n'.format(number)
    f.close()
        
    
|AddProducts()