# СОЗДАЕМ ВИДЖЕТ ENTRY - ЭТО ПОЛЕ ДЛЯ ВВОДА

import tkinter as tk

# 5. создаем функцию для кнопки, которая будет получать информацию

def get_login ():
    value = name.get () # используем метод get, чтобы получить инф. и сохраним в переменную value
    if value:
        print (value)
    else:
        print ('empty value')

# 10. создаем функцию для получения пароля

def get_password ():
    value_2 = password.get () # используем метод get, чтобы получить инф. и сохраним в переменную value
    if value_2:
        print (value_2)
    else:
        print ('empty password')

# 7. создаем функцию для удаления текста в нашем поле ввода Login

def delete_login ():
    name.delete (0, tk.END) # устанавливаем диапазон удаления, от 0 до конца ('end')

# 13. создаем функцию для удаления текста в нашем поле ввода Password

def delete_password ():
    password.delete (0, 'end') # устанавливаем диапазон удаления, от 0 до конца ('end')

# 15. создаем функцию для получения данных из всех строк ввода очищения данных

def submit ():
    print (name.get ())
    print (password.get ())
    delete_password ()
    delete_login ()

root = tk.Tk ()
root.geometry ('300x250')
root.config (bg = 'grey')

# 1. размещаем виджет в окне, вызывая его через класс Entry, и сразу выводя на экран методом grid
# сохраним в переменную name

name = tk.Entry (root)
name.grid (row = 0, column = 1)

# 8. создаем ввод пароля, который будет скрыт

password = tk.Entry (root, show = '*') # значение show скрывает текст, выбрать нужно символ
password.grid (row = 2, column = 1)

# 3. делаем виджет label - Login

lbl1 = tk.Label (root, text = 'Login', bg = 'grey', fg = 'white').grid (row = 0, column = 0, stick = 'w')

# 9. делаем виджет label - Password

lbl2 = tk.Label (root, text = 'Password', bg = 'grey', fg = 'white').grid (row = 2, column = 0, stick = 'w')

# 4. создаем кнопку, которая будет у нас получать информацию Login

tk.Button (root, text = 'get', bg = 'grey', fg = 'white', command = get_login).grid (row = 1, column = 1, stick = 'we')

# 11. создаем кнопку, которая будет у нас получать информацию Password

tk.Button (root, text = 'get', bg = 'grey', fg = 'white', command = get_password).grid (row = 3, column = 1, stick = 'we')

# 6. создаем кнопку удаления Login

tk.Button (root, text = 'delete', bg = 'grey', fg = 'white', command = delete_login).grid (row = 1, column = 0, stick = 'we')

# 12. создаем кнопку удаления Password

tk.Button (root, text = 'delete', bg = 'grey', fg = 'white', command = delete_password).grid (row = 3, column = 0, stick = 'we')

# 14. создаем кнопку представоения - Submit, которая выведет у нас все введенные параметры в строки ввода

tk.Button (root, text = 'submit', bg = 'grey', fg = 'white', command = submit).grid (row = 4, column = 0, stick = 'we')

# 7. создаем кнопку вставки заданного значения, без функции, используем сразу lambda, прописываем значение у insert (место вставки, значение)

tk.Button (root, text = 'insert', bg = 'grey', fg = 'white', command = lambda: name.insert (0, 'roma is a hero')).grid (row = 1, column = 2, stick = 'we')

# 16. создаем кнопку, которая будет закрывать наше окно

close_button = tk.Button (root, text = 'Game Over', bg = 'grey', command = lambda : root.destroy ()).grid (row = 5, column = 0, stick = 'w')

# 2. задаем ширину наших колонок

root.grid_columnconfigure (0, minsize = 100)
root.grid_columnconfigure (1, minsize = 100)
root.grid_columnconfigure (2, minsize = 50)

root.mainloop ()
