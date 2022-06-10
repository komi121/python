"""Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введён после нескольких чисел, 
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу."""

def my_sum (total,*args):
    for element in args:
        total += float(element)
    return total

def check (my_list:list, flag = None):
    if "exit" in my_list:
        flag = False
    else:
        flag = True
    return flag

def string_split(my_string:str):
    return list(my_string.split(" "))

total = 0
while True:
    my_str = input("Введите числа:\n")
    my_list = string_split(my_str)
    if check(my_list):
        total = my_sum(total, *my_list)
        print(total)
        print("Стоп слово 'exit'")
    else:
        total = my_sum(total, *my_list[:len(my_list)-1])
        if len(my_list) != 1:
            print(total)
        break
