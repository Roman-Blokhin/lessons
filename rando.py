import random

num = (random.randint(0,20))

max_try = 5
try_num = 2

print ("Привет, угадай число, которое я загадал =)\n")
while True:
    print(" ")
    print("У тебя осталось", max_try - try_num + 1, "попыток из", max_try)
    #print("Программа загадала: ", num)
    user = int(input("Угадай число: "))

    if user == num:
        print("Все верно, поздравляю!")
        break
    elif try_num > max_try:
        print("Количество попыток исчерпано!")
        break
    elif user <= num:
        print ("Загадай число побольше! ")
    else:
        print("Загадай число поменьше! ")
    try_num = try_num + 1
        
print ("Конец игры.")
