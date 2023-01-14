# Создать кнопку, которая будет менять цвет окна

import tkinter as tk
import random as r

def change ():
    a = r.randint (0, 5)
    if a == 0:
        root.config (bg = 'pink')
    elif a == 1:
        root.config (bg = 'black')
    elif a == 2:
        root.config (bg = 'yellow')
    elif a == 3:
        root.config (bg = 'green')
    elif a == 4:
        root.config (bg = 'red')
    elif a == 5:
        root.config (bg = 'blue')

root = tk.Tk ()
root.geometry ('300x300+100+100')
root.title ('Heroe\'s land')
root.config (bg = 'grey')

btn1 = tk.Button (root, text = 'Change Color', command = change)
btn1.pack ()

root.mainloop ()
