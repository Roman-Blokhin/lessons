# менеджеры контекста with....as

# https://www.youtube.com/watch?v=Uy07s6sEYoM&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&index=15

# когда в программе есть ошибка, программа все равно сработает

with open ('text.txt', 'wt', encoding = 'utf-8') as f:
    a = int (input("Введите число: "))
    b = str ('1 / ' + str (a) + ' = ' + str (1 / a))
    print (b)
    f.write (b)

# критическая функция выполняется, программа выдает ошибку, файл закрывается и пользователь не имеет к нему доступа

# на самом деле, не понял пока, для чего это нужно