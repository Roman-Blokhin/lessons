"""ИЗУЧАЕМ БИБЛИОТЕКУ SIMPLE-DRAW
не поддерживается в python -V > 3.10"""

import simple_draw as sd

sd.resolution = (1000, 200) # устанавливаем размер окна
point = sd.random_point() # можно задать рандомное значение точки, можно: sd.random_point()

sd.circle (center_position = point) # создаем круг с координатами точки

# sd.pause()
