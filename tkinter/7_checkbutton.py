"""Изучаем виджет Checkbutton"""

from tkinter import *

# Прописываем функцию для перебора каждого элемента списка, чтобы активировать галочки
def select_all ():
    for i in [year, marketing, subscribe]:
        i.select () # активирует наши checkbuttons

# Прописываем функцию для перебора каждого элемента списка, чтобы ДЕактивировать галочки
def deselect_all ():
    for i in [year, marketing, subscribe]:
        i.deselect () # ДЕактивирует наши checkbuttons

# Прописываем функцию, чтобы проставить противоположное значение галочек
def toggle_all ():
    for i in [year, marketing, subscribe]:
        i.toggle () # ДЕактивирует наши checkbuttons

root = Tk ()
root.title ('')
root.geometry ('350x350+200+200')
root.config (bg = '')

year = Checkbutton (text = 'Вам исполнилось 18 лет?')
year.pack ()

marketing = Checkbutton (text = 'Хотите получать рекламу?')
marketing.pack ()

subscribe = Checkbutton (text = 'Готовы подписаться??', indicatoron = False)
# indicatoron = False - можно написать : indicatoron = 0, но это будет не совсем корректно
subscribe.pack ()

Button (text = 'Выбрать все галочки', command = select_all).pack ()
Button (text = 'Снять все галочки', command = deselect_all).pack ()
Button (text = 'Противоположное значение галочек', command = toggle_all).pack ()

root.mainloop ()