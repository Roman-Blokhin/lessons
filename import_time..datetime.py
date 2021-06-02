# https://python-scripts.com/datetime-time-python

# МОДУЛЬ datetime

import datetime # импортируем модуль

# 1 - самостоятельно прописываем дату
print (datetime.date (2021, 5, 22)) # по умолчанию идет сначала год, месяц, день
print ("")

# 2 - самостоятельно прописываем дату
d = datetime.date (2021, 5, 22)
print (d.day)
print (d.month)
print (d.year)
print ("")

# 3 - узнать какая дата сейчас, с помощью функции - today

print (datetime.date.today())
print ("")

# 4 - узнать дату и время с помощью функции datetime.datetime.today
# указывается дата и время(до мили-секунд)

a = (datetime.datetime.today())
print (a)
print ("")

# или

b = (datetime.datetime.now())
print (b)
print ("")

# 5 - модуль datetime содержит и другой метод - strftime
# позволяет более понятно вывести параметры

a = datetime.datetime.today()
print (a.strftime("%d.%m.%Y")) # в качестве разделителя можно использовать любые символы

print (a.strftime("%d.%m.%Y. %H.%M")) # МНЕ ПОДХОДИТ
print ("")

# 6 - Чтобы найти разницу в промежутке времени нужно использовать метод datetime.timedelta

now = datetime.datetime.today() # автоматическое определение времени сейчас
then = datetime.datetime (2021, 5, 25) # задаем нужную дату
delta = then - a  # высчитываем разницу

print (delta) # общая (и дни, и секунды)
print (delta.days) # дни
print (delta.seconds) # секунды
print ("")

seconds = delta.total_seconds()
hours = int(seconds // 3600)
print("Осталось часов: " + str(hours))
minutes = int((seconds % 3600) // 60)
print("Осталось минут: " + str(minutes))
print("")

# 7 - модуль time - позволяет выводить время

import time

print (time.ctime()) # выводит сегодняшнюю дату и время(немного коряво) - пустое значение
print (time.ctime(9976284875)) # самая ранняя дата 1970 год 3.00, от этой даты считает сек

# метод - time.sleep - позволяет ставить паузу, например - закрыть программу

for i in range (1): # 10 раз выводит наше послание пользователь каждые 60 секунд
    time.sleep (2)
    print ("\nПришло время отдохнуть")
    print ("")

# метод - time.strftime - помогает выводить время и дату
z = time.strftime("%d.%m.%Y %H.%M", time.localtime()) # местное
u = time.strftime ("%d.%m.%Y %H.%M", time.gmtime()) # по мировому стандарту
print(z)
print(u)
print ("")

# метод - time.time - отображает время в секундах, начиная с начала эпохи 1970г

x = time.time ()
print (x)
print ("")

# можно использовать метод ctime для преобразование в дату и время.
# пока не понял, как мне это пригодится

a = time.ctime(time.time())
print(a)
