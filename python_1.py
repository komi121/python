"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

def my_division ( dividend, divisor):
    """ The function divides dividend by divisor
    Usage: my_division(a, b) """
    try:
        return (dividend / divisor)
    except ZeroDivisionError:
        print("На ноль делить нельзя")
        return None


dividend = float(input("Введите делимое: "))
divisor = float(input("Введите делитель: "))

flag = True

while flag:
    if divisor == 0:
        print("На ноль делить нельзя")
        divisor = float(input("Введите делитель: "))
    else:
        flag = False

print(my_division(dividend, divisor))
