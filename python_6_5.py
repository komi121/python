"""5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. 
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""


class Stationery:
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print("так может нарисовать любой предмет")

class Pen(Stationery):
    def __init__(self,title):
        super().__init__(title)
    
    def draw(self):
        print("так рисует только ручка")


class Pencil(Stationery):
    def __init__(self,title):
        super().__init__(title)
    
    def draw(self):
        print("так рисует только карандаш")


class Handle(Stationery):
    def __init__(self,title):
        super().__init__(title)
    
    def draw(self):
        print("так рисует только маркер")


stationery = Stationery("краска")
pen = Pen("ручка")
handle = Handle("маркер")
pencil = Pencil("карандаш")
stationery.draw()
pen.draw()
handle.draw()
pencil.draw()

