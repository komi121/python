""""Реализовать функцию my_func(), которая принимает три позиционных аргумента и 
возвращает сумму наибольших двух аргументов."""

def my_func(var_1, var_2, var_3):
    """The function returns the sum of the two largest numbers"""
    summ = var_1 + var_2 + var_3 - min(var_1, var_2, var_3)
    return summ

print(my_func(2, 4, 0))
print(my_func(-2, 41, 0))
print(my_func(-2, 41, -12))
print(my_func(0, 4, 0))
print(my_func(1, 4, 1))
