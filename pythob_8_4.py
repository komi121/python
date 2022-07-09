""" Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определите параметры, общие для приведённых типов. 
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники."""

""" 5. Продолжить работу над первым заданием. 
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
 Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, 
 можно использовать любую подходящую структуру (например, словарь)."""

class CheckInt(Exception):
    def __init__(self, text):
        self.text = text

class Stock :
    def __init__ (self, value):
        self.value = value
        self.info = dict()
    def get_value(self):
        return self.value
    def get_stock(self,tag, number):
        self.info[tag] = number

    

class Tech : 
    def __init__(self, tag, price, product, count, val):
        self.tag = tag
        self.price = price
        self.product = product
        self.count = count
        self.val = int(val)
    def get_price(self):
        return int(self.price)
    def get_tag(self):
        return self.tag
    def get_stock(self, other):
        other.value += self.val
        while True:
            number = input("введите единиц для хранения: ")
            try:
                number = int(number)
            except ValueError as warrning:
                try:
                    raise CheckInt("Это не число")
                except CheckInt as war:
                    print(war)
            else:
                break
        other.get_stock(self.tag, number)
    


class Printer(Tech):
    def __init__(self, tag, price, product, count, number_list, val):
        super().__init__(tag,price,product,count, val)
        self.number_list = number_list
    def get_price(self):
        return int(self.price) * int(self.count)

class Scaner ( Tech):
    def __init__(self, tag, price, product, count, speed, val):
        super().__init__(tag,price,product,count, val)
        self.speed = speed

class Xerox(Tech):
    def __init__(self, tag, price, product, count, speed, number_list, val):
        super().__init__(tag,price,product,count, val)
        self.number_list = number_list
        self.speed  = speed


    
stock1 = Stock(10000)
xcerox = Xerox("xerox_2030",200,"v.12.1",23,23.23,43,100)

xcerox.get_stock(stock1)
print(stock1.info)



