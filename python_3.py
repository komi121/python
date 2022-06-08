"""Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и dict."""

number = int(input("Введите номер месяца:\n"))

season = ["Зима", "Весна", "Лето", "Осень"]
month_l = [[12, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [9, 10, 11]]

for element in range(4):
    if number in month_l[element]:
        print("Способ list:", season[element])

month_d = dict(zip(season, month_l))

for key in month_d:
    if number in month_d[key]:
        print("Способ dict:",key)
