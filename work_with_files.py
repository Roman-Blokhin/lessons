# написать программу и подключить к ней новый текстовый файл для сбора данных от пользователей

# https://www.youtube.com/watch?v=ypoE3bD2xbI&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&index=14

# придется все закомментировать, иначе не будет работать

# 1
# в новой папке, отведенной под новый проект, можно создать новый текстовый документ, для дальнейшего его использования, либо написать код, чтобы новый файл был создан автоматически:

# можно с помощью функции - write - написать новый текст, взамен старого

#f = open ('text.txt', 'w')
#print (f.write ("Hi, my name is a hero"))
#f.close () 


# 2
# Данный код позволяет(функция - read) прочитать файл, либо указать кол-во символов, которое нужно вывести в консоли:

#f = open ('text.txt')
#print (f.read (5)) 

# 3
# можем выводить все строки по порядку из текстового файла

#f = open ('text.txt')
#for a in f:
#    print (a)
#f.close ()

# 4
# таким образом можно запрашивать у пользователя данный, допустим логин и пароль, и сохранять их в отдельный файл, либо другие данные

f = open ('text.txt', "w")
a = f.write (input ("Введите логин: ") + "\n")
print ()
b = f.write (input ("Введите пароль: "))
f.close ()

# 5
# Есть несколько аргументов, которые пишутся вторым после названия текстового файла:

#'r' - открытие на чтение (является значением по умолчанию).
#'w' - открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.
#'x' - открытие на запись, если файла не существует, иначе исключение.
#'a' - открытие на дозапись, информация добавляется в конец файла.
#'b' - открытие в двоичном режиме.
#'t' - открытие в текстовом режиме (является значением по умолчанию).
#'+' - открытие на чтение и запись