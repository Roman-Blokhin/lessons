#Создание виджета Entry

# https://www.youtube.com/watch?v=5C7K5kCxyVM&list=PLQAt0m1f9OHsd6U5okp1XLoYyQR0oBjMM&index=5

import tkinter as tk

# создали стандартное окно
win = tk.Tk ()
win.title ('Виджет Entry')
win.geometry ('400x500+50+50')
#####################################################

# создаем функцию для получения информации
def get_entry ():
	value = name.get ()
	if value:
		print (value)
	else:
		print ('Пустой ввод')
	
# можно сделать вывод в программу мразу нескольких полей
def submit ():
	print (name.get ())
	print (password.get ())
	delete_entry ()
	password.delete (0, tk.END)

# создаем функцию для удаления информации для поля ввода, также прописываем что удалять, в данном случае с нулевого индекса и до конца(весь текст) - можно написать tk.END, а можно 'end'
def delete_entry ():
	name.delete (0, tk.END)

#####################################################

# сщздали текстовый элемент и расположили его в первой строке и первой колонке, прижатым к левой стороне, опубликовали с помощью виджета grid
tk.Label (win, text = "login:").grid (row = 0, column = 0, stick = 'w')
tk.Label (win, text = "Password:").grid (row = 1, column = 0, stick = 'w')

# создали переменную, в которую вложили виджет Entry -для ввода данных на экране и вывели его с помощью виджета grid
name = tk.Entry (win)
# добавляем св-во - show - чтобы наш пароль был закрыт звездочками
password = tk.Entry (win, show = '*')
name.grid(row = 0, column = 1)
password.grid(row = 1, column = 1)

# создаем кнопку для получения информации после ввода, прописываем комманду для получения информации из нашего поля - Entry
tk.Button (win, text = 'Получить',
		  command = get_entry).grid(row = 2, column = 0, stick = 'we')

tk.Button (win, text = 'Войти',
		  command = submit).grid(row = 3, column = 0, stick = 'we')

# создаем кнопку для удаления информации из поля ввода
tk.Button (win, text = 'Удалить', command = delete_entry).grid(row = 2, column = 1, stick = 'we')
tk.Button (win, text = 'Вставить', command = lambda: name.insert (0, 'hello')).grid(row = 2, column = 2, stick = 'we')

# есть метод, который позволяет вставлять определенные значения - insert


# ставим размеры наших колонок
win.grid_columnconfigure (0, minsize = 50)
win.grid_columnconfigure (1, minsize = 100)

#####################################################

win.mainloop ()
