"""Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции."""

number = int(input("Введите целое положительное число:\n"))

quant_number = len(str(number))
max = 0
var_1 = 10

while quant_number:
    per = int("1" + "0" * (quant_number - 1))
    var_2 = number // per
    var = var_2 % var_1
    if var >= max :
        max = var
    quant_number -= 1

print(max)
