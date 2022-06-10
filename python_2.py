"""Выполнить функцию, которая принимает несколько параметров, описывающих 
данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Осуществить вывод данных о пользователе одной строкой."""

def join_data (first_name = None, 
               last_name = None, 
               year_of_birth = None,
               city_of_residence = None,
               email = None,
               phone = None
               ):
    """ Function concatenates named objects into one string"""
    my_str = f"{first_name} {last_name} {year_of_birth} {city_of_residence} {email} {phone}"
    return my_str


data_reference = ["first_name", "last_name", "year_of_birth", "city_of_residence", "email", "phone"]

data_user = list(input("Введите данные пользователя через пробел:").split())
data = dict(zip(data_reference, data_user))

print(join_data(**data))
