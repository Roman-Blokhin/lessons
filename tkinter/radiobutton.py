"""Lesson about Radiobutton"""

from tkinter import *

# 5. создаем функцию для вывода информации в нашем окне, а также консоли
def select_level ():
    level = level_var.get ()
    if level == 1:
        print ('Easy')
    elif level == 2:
        print ('Middle')
    elif level == 3:
        print ('Hard')

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
Radiobutton(text='Easy', bg='pink', font=('Arial', 15), variable=level_var, value=1, command=select_level)\
    .grid(row=1, column=0)
Radiobutton(text='Middle', bg='pink', font=('Arial', 15), variable=level_var, value=2, command=select_level)\
    .grid(row=1, column=1)
Radiobutton(text='Hard', bg='pink', font=('Arial', 15), variable=level_var, value=3, command=select_level)\
    .grid(row=1, column=2)

root.mainloop()
