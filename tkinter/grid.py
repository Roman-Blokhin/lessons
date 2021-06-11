# как размещать виджеты припомощи метода grid
# https://www.youtube.com/watch?v=_7F6FsbJepo&list=PLQAt0m1f9OHsd6U5okp1XLoYyQR0oBjMM&index=4
import tkinter as tk

win = tk.Tk ()
win.geometry ('300x400+100+100')
win.title ('Виджет grid')
win.config (bg = '#5486b8')

###############################################################

btn1 = tk.Button (win, text = 'Hero',
				 bg = '#3da893')
btn2 = tk.Button (win, text = 'Hero',
				 bg = '#b2c73e')

btn3 = tk.Button (win, text = 'Hero',
				 bg = '#3da893')

btn4 = tk.Button (win, text = 'Hero Roman',
				 bg = '#b2c73e')

btn5 = tk.Button (win, text = 'Hero',
				 bg = '#3da893')

btn6 = tk.Button (win, text = 'Hero',
				 bg = '#b2c73e')

btn7 = tk.Button (win, text = 'Hero',
				 bg = 'pink')

btn8 = tk.Button (win, text = 'Hero',
				 bg = 'pink')


# grid - метод, позволяющий располагать наши виджеты в виде таблицы, ставится вместо pack (),
# чтобы расположить как нам надо наш виджет, нужно для grid использовать  2 значения - row и column, они начинаются с нуля
btn1.grid (row = 0, column = 0)
# если нужно притянуть кнопку в какую-то сторону, используем метод stick
btn2.grid (row = 0, column = 1, stick = 'w')
btn3.grid (row = 1, column = 0, stick = 'we')
btn4.grid (row = 1, column = 1)
btn5.grid (row = 2, column = 0)
# если нужно притянуть кнопку в какую-то сторону, используем метод stick
btn6.grid (row = 2, column = 1, stick = 'e')
# чтобы растянуть виджет на несколько колонок - columnspan, он объединяет вправо(в значение даем количество колонок), метод stick растягивает полностью на все колонки(ему передаем стороны света - n, s ,w, e)
btn7.grid (row = 3, column = 0, columnspan = 2, stick = 'we')
# если нужно объеденить ряды, используем - rowspan, объединяет вниз
btn8.grid (row = 0, column = 2, rowspan = 4, stick = 'sn')

# мы можем использовать минимальные значения для колонок с помощью метода - .grid_columnconfigure, сначала задаем индекс колонки, а потом размер:
win.grid_columnconfigure (0, minsize = 100)

############################################################

#можно использовать более быстрый путь создания кнопок(как таблица)

#for i in range (10):
#	for j in range (3):
#		tk.Button (win, text = f'Roma').grid (row = i, column = j, stick = "we")
#
#win.grid_columnconfigure (0, minsize = 100)
#win.grid_columnconfigure (1, minsize = 50)
#win.grid_columnconfigure (2, minsize = 70)


############################################################
win.mainloop ()