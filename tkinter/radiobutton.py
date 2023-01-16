"""Lesson about Radiobutton"""

from tkinter import *

root = Tk()
root.title('Radiobutton')
root.geometry('350x100+200+200')
root.config(bg='pink')

# 2. создаем числовую переменную и привязываем ее ко всем нашим radiobuttons
level_var = IntVar ()

# 1. создаем Label и Radiobuttons
Label(text='Выберите уровень сложности: ', bg = 'pink', font = ('Arial', 15)).grid(row=0, column=0, columnspan=3)

# 3. добавляем атрибут value, чтобы мы могли присвоить значение нашим кнопкам, и они стали нажиматься
Radiobutton(text='Easy', bg = 'pink', font = ('Arial', 15), variable = level_var, value = 1).grid(row=1, column=0)
Radiobutton(text='Middle', bg = 'pink', font = ('Arial', 15), variable = level_var, value = 2).grid(row=1, column=1)
Radiobutton(text='Hard', bg = 'pink', font = ('Arial', 15), variable = level_var, value = 3).grid(row=1, column=2)

root.mainloop()
