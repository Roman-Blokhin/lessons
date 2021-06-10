# Основы ООП 

#https://www.youtube.com/watch?v=CWSgQcIF--8&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&index=17

# создаем класс
class Person:
	name = "Ivan"
	age = 10
	# в классе можно создавать функцию, обяз должен присутствовать аргумент - self
	def set (self, name, age):
		self.name = name
		self.age = age
		
# можно создать новый класс и присвоить ему значение ранее созданного класса - это называется - НАСЛЕДОВАНИЕ
class Student (Person):
	course = 1
	
	def set (self, name, age, course):
		self.name = name
		self.age = age
		self.course = course
	
nik = Student ()
nik.set ('Nikita', 40, 5)
print (nik.name, nik.course, nik.age)
	
# можно использовать новые значения, с помощью функции
igor = Person ()
igor.set ("Igor", 18)
print (igor.name, igor.age)
# создали объект класса Person
vlad = Person ()
vlad.name = "Влад"
print (vlad.name)
# если мы пропишем новый объект, он будет принимать значение своего класса по умолчанию
roman = Person ()
roman.age = 33
roman.name = "Roman"
print (roman.name, roman.age)
# объектов может быть сколько угодно

# НАСЛЕДОВАНИЕ. ИНКАПСУЛЯЦИЯ, пОЛИМОРФИЗМ

# Наследование - когда один класс наследует все значения другого класса
# инкапсуляция - когда нам нужно защитить какую-то переменную , мы пишем ее с нижним подчеркиванием _name 
#это говорит другим разработчикам, что не рекомендуется использовать этот элемент, но в питоне, это не жесткое правило и действия оно не ограничивает, а только рекомендует не использовать элемент

# Полиморфизм - метод, который делает одно и тоже, но в разных типах данных, относительно их специфики
# ПРИМЕР: print (2 + 2) и print ('2' + '2') в данном случае плюс является полиморфизмом

# Переопределение
anna = Student ()
anna.set ('Аня', 15, 5)
print ("Имя: " + anna.name, "Курс: " + str (anna.course), 'Возраст: ' + str (anna.age))