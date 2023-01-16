"""Lesson about Radiobutton"""

from tkinter import *

# 5. создаем функции для вывода информации в нашем окне, а также консоли
def vals_1 ():
    Label (text = 'Выбран 1 уровень сложности', bg='pink').grid (row=2, column=0, columnspan=3, sticky='w')
    print ('1 уровень')

def vals_2 ():
    Label (text = 'Выбран 2 уровень сложности', bg='pink').grid (row=2, column=0, columnspan=3, sticky='w')
    print ('2 уровень')

def vals_3 ():
    Label (text = 'Выбран 3 уровень сложности', bg='pink').grid (row=2, column=0, columnspan=3, sticky='w')
    print ('3 уровень')

root = Tk()
root.title('Radiobutton')
root.geometry('350x100+200+200')
root.config(bg='pink')

# 2. создаем числовую переменную и привязываем ее ко всем нашим radiobuttons
level_var = IntVar()

# 1. создаем Label и Radiobuttons
Label(text='Выберите уровень сложности: ', bg='pink', font=('Arial', 15)).grid(row=0, column=0, columnspan=3)

# 3. добавляем атрибут value, чтобы мы могли присвоить значение нашим кнопкам, и они стали нажиматься
# 4. создаем команду, чтобы понять, какая кнопка нажата
Radiobutton(text='Easy', bg='pink', font=('Arial', 15), variable=level_var, value=1, command=vals_1)\
    .grid(row=1, column=0)
Radiobutton(text='Middle', bg='pink', font=('Arial', 15), variable=level_var, value=2, command=vals_2)\
    .grid(row=1, column=1)
Radiobutton(text='Hard', bg='pink', font=('Arial', 15), variable=level_var, value=3, command=vals_3)\
    .grid(row=1, column=2)

root.mainloop()
