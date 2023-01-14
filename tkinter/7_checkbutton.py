"""Изучаем виджет Checkbutton"""

from tkinter import *


# ---------------------------------------------------- 2. ФУНКЦИИ

# Прописываем функцию для перебора каждого элемента списка, чтобы активировать галочки
def select_all():
    for i in [year, marketing, subscribe]:
        i.select()  # активирует наши checkbuttons


# Прописываем функцию для перебора каждого элемента списка, чтобы ДЕактивировать галочки
def deselect_all():
    for i in [year, marketing, subscribe]:
        i.deselect()  # ДЕактивирует наши checkbuttons


# Прописываем функцию, чтобы проставить противоположное значение галочек
def toggle_all():
    for i in [year, marketing, subscribe]:
        i.toggle()  # ДЕактивирует наши checkbuttons


# 6. создаем переменную, чтобы получать значение наших переменных и видеть, нажат ли флажок
def show():
    print('флажок year: ', year_value.get())


# ---------------------------------------------------- НАШЕ ОКНО

root = Tk()

root.title('')
root.geometry('350x350+200+200')
root.config(bg='')

# ---------------------------------------------------- 3. ПЕРЕМЕННЫЕ

# создаем переменные, чтобы можно было получать наши данные в консоль
year_value = StringVar()
year_value.set('NO')  # 7. устанавливаем начальное значение флажка
marketing_value = IntVar()

# ---------------------------------------------------- 1. ВИДЖЕТЫ

# 4. связываем переменную с виджетом с помощью variable
year = Checkbutton(text='Вам исполнилось 18 лет?',
                   variable=year_value,
                   onvalue='YES',  # атрибут говорит, что кнопка нажата
                   offvalue='NO')  # атрибут говорит, что кнопка не нажата
year.pack()

marketing = Checkbutton(text='Хотите получать рекламу?')
marketing.pack()

subscribe = Checkbutton(text='Готовы подписаться??', indicatoron=False)
# indicatoron = False - можно написать : indicatoron = 0, но это будет не совсем корректно
subscribe.pack()

Button(text='Выбрать все галочки', command=select_all).pack()
Button(text='Снять все галочки', command=deselect_all).pack()
Button(text='Противоположное значение галочек', command=toggle_all).pack()

# 5. кнопка, чтобы видеть значения наших флажков в консоли
Button(text='Просмотр значений', command=show).pack()

# ---------------------------------------------------- ВАЖНОЕ

root.mainloop()
