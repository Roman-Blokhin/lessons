# ИСКЛЮЧЕНИЯ

# https://www.youtube.com/watch?v=KTosYqzyLpU&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&index=13

# напишем простой калькулятор, чтобы использовать исклюения во времяделения на ноль и вводе чисел для вычислений

while True:
    try:
        a = int (input ("\nВведите первое число: "))
    except ValueError: # вписываем возможную ошибку, чтобы при выводе программы она не выводилась, а работа продолжалась
        print ("Вы ввели не число\n")
        a = 0
        
    try:
        b = int (input ("Введите второе число: "))
    except ValueError:
        print ("Вы ввели не число")
        b = 0
#    else: # выводится, когда не возникает ошибки
#        print ("Все верно")
#    finally: # всегда выводится, не зависимо, есть ли ошибка
#        ("Всегда выводится")
    
    try:
        res = a / b
    except ZeroDivisionError:
        print ()
        res = 0 # нужно, чтобы программа в цикле выводила правильный результат
        
    try:
        print ("Ваш результат: " + str(res))
    except NameError:
        print ("Результат не вычисляем\n")
    
    c = input ("""\nВыберите действие:
1. Повторить расчет
2. Выход 
""")
    if c == "2":
        break
