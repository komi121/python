"""2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
 К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: 
 размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

class Clothes:
    fabrics = 0
    def coat(self,v):
        area = v/6.5 + 0.5
        self.fabrics += area
        return area
    def suit(self,h):
        area = 2*h + 0.3
        self.fabrics += area
        return area
    @property
    def sum_area(self):
        return self.fabrics

exm_1 = Clothes()
exm_1.coat(65)
exm_1.suit(20)
print(exm_1.sum_area)


from abc import ABC, abstractmethod
class Cloth(ABC):
    @abstractmethod
    def fabric_area(self, v, h):
        pass
    @abstractmethod
    def parametrs_people(self, w, e):
        pass
    @abstractmethod
    def money (self):
        pass

class Cap(Cloth):
    def fabric_area(self, v, h):
        pass
    def parametrs_people(self, w, e):
        pass
    def money (self):
        pass

mc = Cap()





