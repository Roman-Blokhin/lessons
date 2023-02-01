"""ИЗУЧАЕМ БИБЛИОТЕКУ SIMPLE-DRAW
не поддерживается в python -V > 3.10"""

import simple_draw as sd

sd.resolution = (500, 500) # 1. устанавливаем размер окна
point = sd.random_point() # 2. можно задать рандомные координаты точки
sd.circle (center_position = point, color = sd.COLOR_BLACK, radius = 50, width = 5) # 3. круг с координатами точки

# делаем функцию, которая вызовет 3 круга с шагом 5 пикселей в радиусе
point_2 = sd.get_point (200, 300) # фиксированные координаты
radius = 30
for _ in range (3):
    radius +=5
    # color = sd.random_color() -  дает рандомное значение цвета нашей окружности
    sd.circle (center_position = point_2, color = sd.random_color(), radius = radius, width = 4)





sd.pause()
