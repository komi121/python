""" Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, 
толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т."""

class Road:
    _length = None
    _width = None
    def __init__ (self, length:float, width:float):
        self._length = length
        self._width = width
    
    def massa (self, massa_asphalt:float, thickness:float):
        return self._length * self._width * massa_asphalt * thickness / 1000


rod = Road(20,5000)
print(f"масса асфальта {rod.massa(25,5)} т")
