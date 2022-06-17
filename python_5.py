"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран."""

n = int(input())


def sum_list(*args):
    summ = 0
    for element in args:
        summ += float(element)
    return summ


with open("python_5.txt", "w") as data_number:
    for x in range(1, n + 1):
        data_number.write(str(x) + " ")

with open("python_5.txt", "r") as data_number:
    my_list = (data_number.readline().split())
    result = sum_list(*my_list)

print(result)
