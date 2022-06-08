"""Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара
: название, цена, количество, единица измерения. 
Структуру нужно сформировать программно, запросив все данные у пользователя.
Пример готовой структуры:

[
(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
(2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
(3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
Пример:

{
"название": ["компьютер", "принтер", "сканер"],
"цена": [20000, 6000, 2000],
"количество": [5, 2, 7],
"ед": ["шт."]
}"""

index = 1
registry = []
list_charac = ["название","цена","количество","единиц"]
analytics = {key: [] for key in list_charac}

print("Для выхода введите 'exit'\nДля внесения товара в реестр вводите параметры через пробел")
while True:
    in_data = input(f"Введите навзвание, цену, количество и единиц для {index} товара\n")
    if in_data == "exit":
        break
    else:
        product = list(in_data.split(" "))
        registry.append((index,{}))
        for i in range(0,4):
            registry[index - 1][1][list_charac[i]] = product[i]
        index += 1
        print("Товар добавлен")

for key in list_charac:
    for i in range (len(registry)):
        analytics[key].append(registry[i][1][key])

for key in analytics:
    analytics[key] = list(set(analytics[key]))

print("Реестр:")
for i in range (len(registry)):
    print(f"№{i+1}", end = " _ ")
    for key in list_charac:
        print(f"{key}:{registry[i][1][key]}", end = " ")
    print("\n")

print("Аналиика")
for key in analytics:
    print(key, " - ", analytics[key] )
