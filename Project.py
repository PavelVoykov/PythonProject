import re
import random
import time
import os
TottalProfit = 0
TottalProfit = 0
prices = []
names = []
bill = 0
AllCal = []
billCal = 0
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
class Product:
    def __init__(self, name, price, cal, idt):
        self.name = name
        self.price = price
        self.cal = cal
        self.idt = idt


def AddProducts():
    
    random.seed(time.time())
    name = input('This product is called:\n')
    price = input('The price of this product is:\n')
    while re.search(',', price):
        price = input('The price of this product is:\n')
    cal = input('How many calories countains this product?\n')
    number = random.randint(10000000,99999999)
    
    f = open('EveryProduct.txt', 'r')
    for i in f:
        m = re.search('#[1-9]{8}', i)
        if m != 0:
            number = random.randint(10000000,99999999)
            continue
    f.close()
    pro = Product(name, price, cal, number)
    
    

    f = open('EveryProduct.txt', 'a')
    
    pro.idt = str(pro.idt)
    f.write('\n')
    f.write(pro.name)
    f.write(',$')
    f.write(pro.price)
    f.write(',')
    f.write(pro.cal)
    f.write(',#')
    f.write(pro.idt)
    f.close()

def PrintPrices(AllCal, billCal, names, prices, bill):
    cls()
    m = 0   
    print('      Firma EOOD')
    print('\n')
    for i in names:    
        print('{}.......{}........{:.2f}'.format(i, AllCal[m], prices[m]))
        m+=1
    print('\n=========================')
    print('+++++++++++++++++++++++++')     
    print('=========================') 
    print('\nTOTTAL PRICE:{:.2f}'.format(bill))
    print('TOTTAL CALORIES:{}'.format(billCal))
    input('\n\nPress "Enter" to finish\n')
    cls()
def Make(TottalProfit):
    cls()
    Calories = 0
    txtprice = ''
    global prices
    global names
    global bill
    global AllCal
    global billCal
    name = ''
    
    prod = input('Product ID\n')
    while prod:
        f = open('EveryProduct.txt', 'r')
        for i in f:
            m = re.search('#{}'.format(prod), i)
            if m != None:
                if re.search('\$[0-9]+\.[0-9]{2}', i):
                    txtprice = re.search('\$[0-9]+\.[0-9]{2}', i)
                    txtprice = re.search('[0-9]+\.[0-9]{2}', txtprice.group())
                    txtprice = txtprice.group()
                    txtprice = float(txtprice)
                    name = re.search('[a-zA-Z]+', i)
                    Calories = re.search(',[0-9]+', i)
                    Calories = re.search('[0-9]+', Calories.group())
                    Calories = Calories.group()
                    Calories = int(Calories)
                    AllCal.append(Calories)
                    names.append(name.group())
                    prices.append(txtprice)
                    cls()
                elif re.search('\$[1-9]+', i):
                    txtprice = re.search('\$[1-9]+,', i)
                    txtprice = re.search('[1-9]+', txtprice.group())
                    txtprice = txtprice.group()
                    txtprice = float(txtprice)
                    name = re.search('[a-zA-Z]+', i)
                    Calories = re.search(',[1-9]+', i)
                    Calories = re.search('[1-9]+', Calories.group())
                    Calories = Calories.group()
                    Calories = int(Calories)
                    AllCal.append(Calories)
                    names.append(name.group())
                    prices.append(txtprice)
                    cls()
                    
                    
        f.close()
        prod = input('Product ID\n')
        q = 0
    for i in prices:
        billCal += AllCal[q]
        bill += i
        TottalProfit += i
        q+=1
   
def MakeByNum(Num):
    cls()
    global prices
    global names
    global bill
    global AllCal
    global billCal
    
    while Num:
        p = input('Enter price\n')
        while re.search(',', p):
            p = input('Enter price\n')
        c = input('Enter calories\n')
        p = float(p)
        c = int(c)
        prices.append(p)
        AllCal.append(c)
        billCal += c
        bill += p
        
        if Num == '1':
            names.append('Drinks')
        elif Num == '2':
            names.append('Meat')
        elif Num == '3':
            names.append('Vegetables')
        elif Num == '4':
            names.append('Snacks')
        Num = input()
        cls()
    
   
def main():
    act = input()
    while act != 'Add' and act != 'New' and act != '1' and act != '2' and act != '3' and act != '4':
        cls()
        act  = input('Invalid input! Try again!')
    while act == 'Add' or act == 'New' or act == '1' or act == '2' or act == '3' or act == '4':
        if act == 'Add':
            AddProducts()
            cls()
        if act == 'New':
            Make(TottalProfit)
            cls()
        if act == '1' or act == '2' or act == '3' or act == '4':
            MakeByNum(act)
        act  = input()
    PrintPrices(AllCal, billCal, names, prices, bill)
main()
