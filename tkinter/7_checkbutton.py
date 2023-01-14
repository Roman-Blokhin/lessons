"""Изучаем виджет Checkbutton"""

from tkinter import *

root = Tk ()
root.title ('')
root.geometry ('350x350+200+200')
root.config (bg = '')

Checkbutton (text = 'Вам исполнилось 18 лет?').pack ()
Checkbutton (text = 'Хотите получать рекламу?').pack ()
Checkbutton (text = 'Готовы подписаться??').pack ()

root.mainloop ()