# Урок 3. Виджет Button
# https://www.youtube.com/watch?v=_pUeSkDMY6w

import tkinter as tk

# для кнопки 1 мы пишем функцию, которая в консоль выводит текст
def hello ():
	print ('hero')

# для кнопки 2 мы пишем функцию с лейблом
def label ():
	la = tk.Label (win, text = 'Roman',
			      bg = '#a3a32c',
			   	  fg = "#235a99",
		          font = ('Arial', 20, 'bold'))
	la.pack ()
# функция для кнопки - счетчика btn_4	
def counter ():
	global count
	count += 1
	btn_4 ['text'] = f'Счетчик: {count}'

# переменная для нашей 4 кнопки(счетчик)
count = 0

# создаем стандартное окно (Lable добавил в качестве практики от прошлых уроков)

win = tk.Tk ()
win.title ('Виджет Button')
win.config (bg = '#63635b')
win.geometry ('400x500+100+100')
#la = tk.Label (win, text = 'Roman',
#			   bg = '#a3a32c',
#			   fg = "#235a99",
#			   font = ('Arial', 20, 'bold'))
#la.pack ()

# создаем кнопку, указываем окно и тип - текст.
btn_1 = tk.Button (win, text = 'Hello',
				command = hello)
btn_2 = tk.Button (win, text = 'Roman',
				command = label)
# можно делать кнопки, используя функцию лямбда, тогда код должен быть в одну строчку и не нужно создавать дополнительных отдельных функций
btn_3 = tk.Button (win, text = 'lambda',
				command = lambda: tk.Label (win, text = 'lambda roman', bg = '#a3a32c').pack ())
# свойство - activebackground - меняет цвет кнопки при нажатии
# свойство - state - не дает нажать на кнопку - state = tk.DISABLED или NORMAL

btn_4 = tk.Button (win, text = f'Счетчик: {count}',
				command = counter,
				  bg = 'red',
				  activebackground = 'blue',
				  state = tk.DISABLED)
# выводим кнопку на наше окно
btn_1.pack ()
btn_2.pack ()
btn_3.pack ()
btn_4.pack ()


win.mainloop ()
