# ЦИКЛ FOR ПОЗВОЛЯЕТ ПРОЙТИСЬ ПО ВСЕМ ЗНАЧЕНИЯМ СЛОВАРЯ, СПИСКА, МНОЖЕСТВА ИЛИ КОРТЕЖИ

zoo = ['Кошка', 'Собака', 'Слон', 'Бегемотик', 'Удав', 'Птерадактиль']
count_animals = 0
letters_count = 0
for i in zoo:
    count_animals +=1
    letters_count += len(i)
    if i == 'Бегемотик':
        continue
    print ('Сейчас система видит животное:', i)
print ('Животных в зоопарке:', count_animals)
print ('Букв в названии животных:', letters_count)

print ('-------------------------------------')

# функция enumerate позволяет пронумеровать наши элементы списка
for j, animal in enumerate (zoo):
    print (j, animal)

print('-------------------------------------')

# можно делать цикл в цикле
for animal in zoo:
    for char in animal:
        if animal == 'Кошка':
            continue
        print (char)

print('-------------------------------------')

# цикл может проходить и по словарям
zoo_dict = {
    'Кошка': 25,
    'Собака': 15,
    'Лошадь': 525,
    'Слон': 1225,
}

total_mass = 0
for animal in zoo_dict:
    mass = zoo_dict [animal]
    total_mass += mass
    print ('Взвешивается:', animal, '-', mass)
print ('Общая масса животных:', total_mass)

print('-------------------------------------')

# можно упростить

total_mass = 0
for animal, mass in zoo_dict.items():
    total_mass += mass
    print ('Взвешивается:', animal, '-', mass)
print ('Общая масса животных:', total_mass)

print('-------------------------------------')

# если нужно вывести только ключи, без значений, пишем так:
total_mass = 0
for mass in zoo_dict.values():
    total_mass += mass
    print (mass)
print ('Общая масса животных:', total_mass)