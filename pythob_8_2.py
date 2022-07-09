"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа 
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class DivZero(Exception):
    def __init__(self,warning):
        self.warning = warning

while True:
    a = int(input())
    b = int(input())
    try:
        if b == 0:
            raise DivZero("На ноль деление")
    except DivZero as warning:
        print(warning)
    else:
        print(a / b)

