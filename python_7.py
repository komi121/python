"""7. Продолжить работу над заданием. 
В программу должна попадать строка из слов, разделённых пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. 
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
Используйте написанную ранее функцию int_func()."""

def int_func(word:str):
    word = word[0].upper() + word[1:]
    return word

def str_spliter (my_str:str):
    my_list = list(my_str.split(" "))
    return my_list

def list_join (my_list:list):
    my_str = " ".join(my_list)
    return my_str

words = input()

list_word = str_spliter(words)

for index in range(len(list_word)):
    list_word[index] = int_func(list_word[index])

print(list_join(list_word))
