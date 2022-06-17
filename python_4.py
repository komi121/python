"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

from base64 import encode


my_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

with open("python_4.txt", "r", encoding="utf-8") as data:
    data_russian = open("python_4_ru.txt", "a", encoding="utf-8")
    for string in data:
        my_list = string.split()
        my_list[0] = my_dict[my_list[0]]
        my_list.append("\n")
        data_russian.write(" ".join(my_list))
    data_russian.close()
