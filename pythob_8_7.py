""" 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». 
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. 
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата."""


class ComplexInt:
    def __init__(self, comp_string):
        list_comp = comp_string.split()
        self.a = int(list_comp[0])
        self.b = int(list_comp[2][0:-1])
    def __str__(self) -> str:
        if self.b > 0:
            return str(self.a) + " + " + str(self.b) + "i"
        if self.b < 0:
            return str(self.a) + " - " + str(abs(self.b)) + "i"

    def __add__ (self,other):
        self.a += other.a
        self.b += other.b
    def __mul__ (self, other):
        self.a = (self.a * other.a) - (self.b * other.b)
        self.b = (self.b * other.a) + (self.a * other.b)
    
com = ComplexInt("12 + 32i")
com2 = ComplexInt("1 + 3i")
com + com2
print(com)
com * com2 
print(com)
