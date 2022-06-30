""" 1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск); атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, 
третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. 
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time


class TrafficLight:
    __color = {0 : 1,
               1 : 1,
               2 : 1}
    __mode_auto = ["Красный","Желтый","Зеленый" ]
    __mode = ["Красный","Желтый","Зеленый","Желтый" ]
    def __init__(self):
        self.__flag_hist = None

    def running_auto(self):
        for index in range(len(self.__mode_auto)):
            self.__flag = self.__mode_auto[index]
            print(f"Сейчас горит {self.__flag}")
            print(f"Осталось гореть {self.__color[index]} сек")
            time.sleep(self.__color[index])


    def running(self):
        if self.__flag_hist in [0,1]:
            self.__flag_hist += 1
            print(f"Сейчас горит {self.__mode[self.__flag_hist]}")
            print(f"Осталось гореть {self.__color[self.__flag_hist]} сек")
            time.sleep(self.__color[self.__flag_hist])
        elif self.__flag_hist == 2:
            self.__flag_hist = 1
            print(f"Сейчас горит {self.__mode[self.__flag_hist]}")
            print(f"Осталось гореть {self.__color[self.__flag_hist]} сек")
            time.sleep(self.__color[self.__flag_hist])
            self.__flag_hist = None
        else:
            self.__flag_hist = 0
            print(f"Сейчас горит {self.__mode[self.__flag_hist]}")
            print(f"Осталось гореть {self.__color[self.__flag_hist]} сек")
            time.sleep(self.__color[self.__flag_hist])


example = TrafficLight()
example.running()
example.running()
example.running()
example2 = TrafficLight()
example.running()
example2.running()
example.running()
example2.running()
example.running()
example2.running()
example.running()
example.running_auto()
# я не совсем понял проверку режимов, светофор у нас автоматически переключается, а пользователь задает цвет
