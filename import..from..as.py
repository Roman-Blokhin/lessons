# МОДУЛИ. РАБОТА С import и from

# https://www.youtube.com/watch?v=V3-3xjtMB48&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&index=16

# когда мы импортируем модуль, можно указывать псевдоним, чтобы постоянно не писать долгое название

import random as r 

# если вы не уверены в названии модуля, чтобы программа не выдавала ошибку, можно использовать исключения try..except
try:
    import nofrtune
except ImportError:
    print ("Модуля - nofrtune - не существует")
    
print (r.random ())

# так же мы можем создать и подключить свой модуль. Для этого нам нужно с этой же папке создать еще один файл формата .py туда написать код или прогграмму и импортировать в данный файл

#для примера я создал файл roma.py  и добавил туда код:
    
#import time as t

#a = t.strftime ('%d.%m.%Y %H.%M')
#print (a)

import roma as ro

# если мы не пропишем ограничения в собственном модуле, то он в данной программе будет считываться и выдаваться по умолчанию сразу, если мы этого не хотим (if 1 > 2:   print ())

ro.t # мы импортировали из собственного модуля конкретный код
print (ro.lin (2, 12)) # так же передаем функцию через print

# мы можем импортировать определенную функцию, и запись будет проще, не нужно уже указывать модуль, к которому мы обращаемся, когда мы хотим вывести на экран программу (я создал в собственном модуле переменную - b - и вложил в нее код для определения времени)

from roma import lin, b

b
print (lin (5, 45)) 