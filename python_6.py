"""Сформировать (не программно) текстовый файл. 
В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий 
по предмету. Сюда должно входить и количество занятий. 
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

number = {str(x) for x in range(10)}


def split_list(my_list):
    for index in range(len(my_list)):
        my_list[index] = my_list[index].split()
    return my_list


def generator_dict(my_list, items_number):
    key_lesson = []
    for list_line in my_list:
        key_lesson.append(list_line[0][0][:-1])
    answer_dict = dict(zip(key_lesson, items_number))
    return answer_dict


def summa_lesson(my_list):
    for index in range(len(my_list)):
        my_list[index] = my_list[index].split("(")
    return my_list


with open("python_6.txt", "r", encoding="utf-8") as file:
    my_list = file.readlines()

split_data = split_list(my_list)
sum_of_hours = 0
list_of_sum_hours = []

for element in split_data:
    element = summa_lesson(element)

for element in split_data:
    for line in element[1:]:
        if line[0][0] in number:
            sum_of_hours += float(line[0])
    list_of_sum_hours.append(sum_of_hours)
    sum_of_hours = 0


print(generator_dict(my_list, list_of_sum_hours))
