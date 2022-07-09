"""   
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата 
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. 
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12.
 Проверить работу полученной структуры на реальных данных.
"""

class Data:
    list_data = []
    def __init__(self,data_string):
        self.data_string = data_string
    
    @classmethod
    def convert_str_int(self,data_string):
        self.list_data = data_string.split("-")
        for element in self.list_data:
            element = int(element)
        return self.list_data
    
    @staticmethod
    def valid_data (data_string):
        list_data = data_string.split("-")
        for element in list_data:
            element = int(element)
        if int(list_data[0]) > 31 or int(list_data[0]) <= 0:
            print("Такого дня не существует")
        if int(list_data[1]) > 12 or int(list_data[1]) <= 0:
            print("Такого месяца не существует")
        if int(list_data[2]) > 2030 or int(list_data[2]) <= 0:
            print("Такого года не существует")
        


data1 = Data("12-2-2020")
data2 = Data("12-0-2020")
data3 = Data("12-2-0")


print(data1.convert_str_int("12-2-2020"))
data2.valid_data("12-0-2020")
data3.valid_data("12-2-0")

