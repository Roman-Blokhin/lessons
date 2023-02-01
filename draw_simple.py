"""ИЗУЧАЕМ БИБЛИОТЕКУ SIMPLE-DRAW
не поддерживается в python -V > 3.10"""
import random

import simple_draw as sd

sd.resolution = (1100, 500) # 1. устанавливаем размер окна
point = sd.random_point() # 2. можно задать рандомные координаты точки
sd.circle (center_position = point, color = sd.COLOR_BLACK, radius = 50, width = 5) # 3. круг с координатами точки

# делаем функцию, которая вызовет 3 круга с шагом 5 пикселей в радиусе
point_2 = sd.get_point (200, 300) # фиксированные координаты
radius = 30
for _ in range (3):
    radius +=5
    # color = sd.random_color() -  дает рандомное значение цвета нашей окружности
    sd.circle (center_position = point_2, color = sd.random_color(), radius = radius, width = 4)

# делаем новую функцию
def bubble (point, step):
    radius = 50
    for _ in range (3):
        radius += step
        sd.circle (center_position = point, color = sd.random_color(), radius = radius, width = 6)
point = sd.get_point (100, 150)
bubble (point = point, step = 10)

# делаем 10 пузырьков в ряд
def bubble (point, step):
    radius = 30
    for _ in range (2):
        radius += step
        sd.circle (center_position = point, color = sd.random_color(), radius = radius, width = 5)
for x in range (50, 550, 50): # задаем параметры шага создания наших колец
    point = sd.get_point(x, 400) # передаем координату шага
    bubble(point=point, step=5)

# делаем 10 пузырьков в 3 ряда
def bubble (point, step):
    radius = 10
    for _ in range (2):
        radius += step
        sd.circle (center_position = point, color = sd.random_color(), radius = radius, width = 5)

for y in range (50, 151, 50): # задаем координату y
    for x in range (650, 950, 30):
        point = sd.get_point(x, y) # добавляем координату y
        bubble(point=point, step=5)

# делаем 100 шариков в рандомных местах
def bubble (point, step):
    radius = 5
    radius += step
    sd.circle (center_position = point, color = sd.random_color(), radius = radius, width = 1)

for _ in range (100):
    point = sd.random_point() # добавляем координату y
    step = random.randint (1, 20) # добавляем разный размер колец
    bubble(point=point, step=step) # меняем шаг на наш рандом



sd.pause() # не закрывают окно
