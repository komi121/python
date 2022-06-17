"""Создать текстовый файл (не программно). 
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32"""

salary = 0

with open("python_3.txt") as data:
    data_list = data.readlines()
    for index in range(len(data_list)):
        data_list[index] = data_list[index].split()
        data_list[index][1] = float(data_list[index][1])
    for string in data_list:
        salary += string[1]
        if string[1] < 20000:
            print(string[0])
    print(salary / len(data_list))
