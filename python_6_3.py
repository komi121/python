"""3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и 
дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, 
проверить значения атрибутов, вызвать методы экземпляров."""

class Worker:
    profit = {"wage": None, 
              "bonus": 20123}
    def __init__(self,name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
        self.profit["wage"] = self._income


class Position (Worker):
    def __init__ (self,name, surname, position, income):
        super().__init__(name, surname, position,income)
    
    def get_full_name(self):
        print(self.name + " " + self.surname)

    def get_total_income(self):
        print(self._income + self.profit["bonus"])


example = Position("Антон","Иванов","Уборщик",120000)
example.get_full_name()
example.get_total_income()
