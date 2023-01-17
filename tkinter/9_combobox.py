from tkinter import *
from tkinter import ttk


def show_value():
    print(combo.get())
    print(num.get())
    if num.get() == '3':
        root.config(bg='black')
    elif combo.get() == 'Воскресенье':
        but.config(fg='white')


weekdays = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
numbers = [1, 2, 3, 4, 5]

root = Tk()
root.title('Combobox')
root.geometry('250x250+200+200')
root.config(bg='grey')

combo = ttk.Combobox(height=5, justify=RIGHT, values=weekdays)
combo.current(0)  # с помощью current по индексу задаем значение, которое будет отображаться по умолчанию
combo.pack()

num = ttk.Combobox(height=5, justify=LEFT, values=numbers)
num.current(4)  # с помощью current по индексу задаем значение, которое будет отображаться по умолчанию
num.pack()

but = Button(text='show_value', bg='green', command=show_value)
but.pack()

root.mainloop()
