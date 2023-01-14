"""Изучаем виджет Checkbutton"""

from tkinter import *

root = Tk ()
root.title ('')
root.geometry ('350x350+200+200')
root.config (bg = '')

Checkbutton (text = 'Вам исполнилось 18 лет?').pack ()
Checkbutton (text = 'Хотите получать рекламу?').pack ()
Checkbutton (text = 'Готовы подписаться??', indicatoron = False).pack ()
# indicatoron = False - можно написать : indicatoron = 0, но это будет не совсем корректно

root.mainloop ()