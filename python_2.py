"""Пользователь вводит время в секундах. 
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк."""

time = int(input("Введите время в секундах:\n"))

hour = time // 3600
mine = (time % 3600) // 60
sec = time - (hour * 3600 + mine * 60)

hour = str(hour)
mine = str(mine)
sec = str(sec)

if len(hour) == 1:
    hour = "0" + hour

if len(mine) == 1:
    mine = "0" + mine

if len(sec) == 1:
    sec = "0" + sec

print(f"{hour}:{mine}:{sec}")
