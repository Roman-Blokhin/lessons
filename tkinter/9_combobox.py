from tkinter import *
from tkinter import ttk

weekdays = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')

root = Tk()
root.title('Combobox')
root.geometry('250x250+200+200')
root.config(bg='grey')

ttk.Combobox(height=5, justify=RIGHT, values=weekdays).pack()

root.mainloop()
