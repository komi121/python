"""Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. 
У пользователя нужно запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2]."""

my_list = [7, 5, 5, 3, 3, 2]
flag = True
flag_2 = True
number = int(input())
temp = number 

if number in my_list:
    my_list.insert(my_list.index(number) + my_list.count(number), number)
elif number > my_list[0]:
    my_list.insert(0,number)
elif number < my_list[-1]:
    my_list.append(number)
else:
    while flag:
        temp += 1
        if temp in my_list:
           my_list.insert(my_list.index(temp) + my_list.count(temp), number)
           break 

print(my_list)
