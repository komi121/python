"""4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, 
повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 
40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Вызовите методы и покажите результат."""

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
    
    def go(self):
        print("Машина поехала")
    
    def stop(self):
        print("Машина остановилась")

    def turn(self,direction):
        print(f"Машина повернула {direction}")
    
    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__ (self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed >= 60:
            print("сообщение о превышении скорости")
        else:
            return super().show_speed()


class WorkCar(Car):
    def __init__ (self, speed, color, name):
        super().__init__(speed, color, name)
    
    def show_speed(self):
        if self.speed >= 40:
            print("сообщение о превышении скорости")
        else:
            return super().show_speed()


class SportCar(Car):
    def __init__ (self, speed, color, name):
        super().__init__(speed, color, name)
    

class PoliceCar(Car):
    def __init__ (self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


work = WorkCar(321,"blue", "nded")
work2 = WorkCar(30, "blue", "Art")
town = TownCar(50, "red", "Tom")
town2 = TownCar(70, "blue and red", "Tom")
sport = SportCar(500, "red", "Tom")
police = PoliceCar(10, "red", "Tom")

work.go()
work.stop()
work.turn("налево")
work.show_speed()
work2.show_speed()
town2.show_speed()
town.show_speed()
print(police.is_police)
print(sport.is_police)


