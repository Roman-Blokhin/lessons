from tkinter import *
from tkinter import ttk

weekdays = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')

root = Tk()
root.title('Combobox')
root.geometry('250x250+200+200')
root.config(bg='grey')

combo = ttk.Combobox(height=5, justify=RIGHT, values=weekdays)
combo.current (0) # с помощью current по индексу задаем значение, которое будет отображаться по умолчанию
combo.pack()

root.mainloop()
