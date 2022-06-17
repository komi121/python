"""Создать текстовый файл (не программно), сохранить в нём несколько строк, 
выполнить подсчёт строк и слов в каждой строке."""

with open("python_2.txt") as file:
    data = file.readlines()
    number_word = []
    number_string = len(data)
    for string in range(len(data)):
        number_word.append(len(data[string].split()))

print(f"Всего строк в файле {number_string}")
for index in range(len(number_word)):
    print(f"В {index + 1} строке {number_word[index]} слов")
