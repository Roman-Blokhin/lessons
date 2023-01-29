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