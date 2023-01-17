"""Lesson about Radiobutton"""

from tkinter import *

# ---------------------------------------------------------------------

# 16. создаем словарь - ключ:значение, чтобы укоротить нашу функцию и profession radiobattons

professions = {
    7: 'Воин',
    8: 'Маг',
    9: 'Лучник'
}

# ---------------------------------------------------------------------

# 5. создаем функцию для вывода информации в нашем окне, а также консоли
def select_level():
    level = level_var.get()
    level_text.set(f'Вы выбрали {level} уровень')  # 8. создаем ф строку для передачи текста нашего label
    if level == 1:
        print('Easy')
    elif level == 2:
        print('Middle')
    elif level == 3:
        print('Hard')


# 11. создаем функцию для вывода информации в нашем окне, а также консоли касательно расы
def select_spesies():
    spesies_var = spesies.get()
    if spesies_var == 4:
        spesies_var = 'Эльф'  # 12. присваиваем числовой переменной текстовое значение для будущей ф строки
        print('Эльф')
    elif spesies_var == 5:
        spesies_var = 'Орк'
        print('Орк')
    elif spesies_var == 6:
        spesies_var = 'Человек'
        print('Человек')
    spesies_text.set(f'Вы выбрали расу: {spesies_var}')  # 13. создаем ф строку для передачи текста нашего label


# 15. новая функция

def select_profession():
    profession_var = profession.get()
    # 17. обращаемся к нашему словарю professions по ключу profession_var (цифры)
    print (professions[profession_var])
    profession_var = (professions[profession_var]) # 18. выводит в окне название профессии, а не ключ (не цифру)
    profession_text.set(f'Вы выбрали профессию: {profession_var}')

# ---------------------------------------------------------------------

root = Tk()
root.title('Radiobutton')
root.geometry('290x300+200+200')
root.config(bg='pink')

# ---------------------------------------------------------------------

# 2. создаем числовую переменную и привязываем ее ко всем нашим radiobuttons
level_var = IntVar()
# 7. создаем переменную, чтобы вывести текст в наше окно
level_text = StringVar()

# 10. создаем числовую переменную и привязываем ее ко всем нашим radiobuttons
spesies = IntVar()
# 11. создаем переменную, чтобы вывести текст в наше окно касательно расы
spesies_text = StringVar()

# 14. новые переменные
profession = IntVar()
profession_text = StringVar()

# ---------------------------------------------------------------------

# 1. создаем Label и Radiobuttons
Label(text='Выберите уровень сложности: ', bg='pink', font=('Arial', 15)).grid(row=0, column=0, columnspan=3)

# 3. добавляем атрибут value, чтобы мы могли присвоить значение нашим кнопкам, и они стали нажиматься
# 4. создаем команду, чтобы понять, какая кнопка нажата
Radiobutton(text='Easy', bg='pink', font=('Arial', 15), variable=level_var, value=1, command=select_level) \
    .grid(row=1, column=0)
Radiobutton(text='Middle', bg='pink', font=('Arial', 15), variable=level_var, value=2, command=select_level) \
    .grid(row=1, column=1)
Radiobutton(text='Hard', bg='pink', font=('Arial', 15), variable=level_var, value=3, command=select_level) \
    .grid(row=1, column=2)

# 6. создаем Label, который будет выводить сообщение после выбора уровня сложности с атрибутом textvariable
Label(bg='pink', textvariable=level_text).grid(row=2, column=0, columnspan=3, stick='w')

# ---------------------------------------------------------------------

# 9. создаем новую группу radiobuttons
Label(text='Выберите расу: ', bg='pink', font=('Arial', 15)).grid(row=3, column=0, columnspan=3)
Radiobutton(text='Эльф', bg='pink', font=('Arial', 15), variable=spesies, value=4, command=select_spesies) \
    .grid(row=4, column=0)
Radiobutton(text='Орк', bg='pink', font=('Arial', 15), variable=spesies, value=5, command=select_spesies) \
    .grid(row=4, column=1)
Radiobutton(text='Человек', bg='pink', font=('Arial', 15), variable=spesies, value=6, command=select_spesies) \
    .grid(row=4, column=2)

# 12. создаем Label, который будет выводить сообщение после выбора расы с атрибутом textvariable
Label(bg='pink', textvariable=spesies_text).grid(row=5, column=0, columnspan=3, stick='w')

# ---------------------------------------------------------------------

# 13. создаем кнопки для выбора профессии, чтобы показать на примере, как их можно компактно прописать

Label(text='Выберите профессию: ', bg='pink', font=('Arial', 15)).grid(row=6, column=0, columnspan=3)

Radiobutton(text='Воин', bg='pink', font=('Arial', 15), variable=profession, value=7, command=select_profession) \
    .grid(row=7, column=0)
Radiobutton(text='Маг', bg='pink', font=('Arial', 15), variable=profession, value=8, command=select_profession) \
    .grid(row=7, column=1)
Radiobutton(text='Лучник', bg='pink', font=('Arial', 15), variable=profession, value=9, command=select_profession) \
    .grid(row=7, column=2)

Label(bg='pink', textvariable=profession_text).grid(row=8, column=0, columnspan=3, stick='w')

# ---------------------------------------------------------------------

root.mainloop()
