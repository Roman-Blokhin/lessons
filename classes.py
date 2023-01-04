# УРОК ПО КЛАССАМ

# создаем родительский класс, где прописываем все нужные методы
class house ():
    '''описание дома'''

    def __init__ (self, street, number): # создается в первую очередь при создании класса, прописываем свойства объекта, который будет создан на базе нашего класса. как  мин. 1 аргумент - self
        '''свойства дома'''
        self.street = street
        self.number = number
        self.age = 17 # можно указать параметр по умолчанию, его не нужно прописывать в аргумент

    def build (self):
        '''строит дом'''
        print ('Дом на улице ' + self.street + ' под номером ' + str (self.number) + ' построен')

    # создаем функцию, которая определяет возраст дома
    def age_of_house (self, year):
        '''возраст дома'''
        self.age += year

house1 = house ('Московская', 20)
house2 = house ('Ленина', 1)

# мы можем обратиться к нашемей переменной и вывести нужный аргумент
print (house1.street)
print (house2.number)
print (house1.age)

# можно обращаться не только к объектам, но и к методам
house1.build ()
house2.build ()

# попробуем понять какой возраст у дома
house1.age_of_house (5)
print (house1.age)

# создаем наследующий класс - потомок
class prospecthouse (house):
    '''дома на проспекте'''
    def __init__ (self, prospect, number):
        super().__init__ (self, number) # функция super помогает связать класс потомок с классом родителем
        self.prospect = prospect

# создаем новый объект
prhouse = prospecthouse ('Космонавтов', 99)

print (prhouse.prospect)
print (prhouse.number)
print (prhouse.age)



