"""Lesson about Radiobutton"""

from tkinter import *

root = Tk()
root.title('Radiobutton')
root.geometry('350x200+200+200')
root.config(bg='pink')

Label(text='Выберите уровень сложности: ', bg = 'pink', font = ('Arial', 15)).grid(row=0, column=0, columnspan=3)

Radiobutton(text='Easy', bg = 'pink', font = ('Arial', 15)).grid(row=1, column=0)
Radiobutton(text='Middle', bg = 'pink', font = ('Arial', 15)).grid(row=1, column=1)
Radiobutton(text='Hard', bg = 'pink', font = ('Arial', 15)).grid(row=1, column=2)

root.mainloop()
