# СОЗДАЕМ ВСПЛЫВАЮЩИЕ ОКНА - ИНФОРМАЦИЯ, ПРЕДУПРЕЖДЕНИЕ, ОШИБКА

import tkinter as tk
import tkinter.messagebox as mb

def ok ():
    text = 'все гуд, чувак'
    mb.showinfo ('информация', text)

def ok1 ():
    text = 'осторожней'
    mb.showwarning ('предупреждение', text)

def ok2 ():
    text = 'кабздеееец'
    mb.showerror ('ошибка', text)


root = tk.Tk ()
root.geometry ('200x200+100+100')

btn1 = tk.Button (root, text = 'info', command = ok).pack ()
btn2 = tk.Button (root, text = 'warning', command = ok1).pack ()
btn3 = tk.Button (root, text = 'error', command = ok2).pack ()

root.mainloop ()
