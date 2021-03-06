# урок 1. Введение в tkinter

import tkinter as tk

# создаем главное окно
win = tk.Tk ()
# можно заменить иконку нашего окна. скачиваем ее в ту же папку и пишем путь к ней. и ОБЯЗАТЕЛЬНО прикрепляем иконку к нашему окну (значение False говорит, что эта иконка применима только к этому окну)
photo = tk.PhotoImage (file = 'icon.png')
win.iconphoto (False, photo)
# задаем заголовок окна
win.title ('Мое первое окно')
# вызываем метод - .geometry -он отвечает за размер нашего окна ('500x600')
# чтобы открывать в конкретном месте наше окно используем параметры +100+200 - нужно писать без отступов, можно размеры вкладывать в переменные и в методе уже использовать переменные
win.geometry ('400x500+100+100')
# можно создать минимальные значения окна и максимальные
win.minsize (350,450)
win.maxsize (550,650)
# наше окно можно растягивать в любую сторону, потому что метод .resizable поумолчанию имеет значение (True, True), если нужно изменить, то значение ставим (False, False)
win.resizable (True, True)
# можно изменить фон окна (bg - background) - цвет можно выбрать на сайте rgb online
win.config (bg = "#4a8dbd")

# обязательно делаем этот цикл, чтобы у наспоявился результат программы
win.mainloop ()
