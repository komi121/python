"""7. Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
 Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста."""
import json


sum_profit = 0
firm_with_profit = 0
json_list = [{}, {}]

with open("python_7.txt", "r", encoding="utf-8") as data_firm:
    list_firm = []
    for element in data_firm:
        list_firm.append(element.split())

for firma in list_firm:
    firma.append(float(firma[2]) - float(firma[3]))

for element in list_firm:
    json_list[0][element[0]] = element[4]
    if element[4] > 0:
        sum_profit += element[4]
        firm_with_profit += 1

json_list[1]["average_profit"] = sum_profit / firm_with_profit

with open("json_data.txt", "w") as output:
    json.dump(json_list, output)
