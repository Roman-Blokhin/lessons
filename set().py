# МНОЖЕСТВА - set
# в множестве нет повторяющихся элементов
# все элементы выводятся в случайном порядке
########

a = set()
print (type(a))
print (a)
print("")

b = {"23, 32"} # также множества можно записывать так, через запятую
print (type(b))
print (b)
print("")

с = {i ** 2 for i in range(10)} # цикл в множестве
print (type(с))
print (с)
print("")

# frozenset () - множество, в которое нельзя вносить изменения, будет ошибка
# функция - add - добавляет новый элемент в множество

d = set ("hero")
e = frozenset ("roman")
d.add (12)
print (d)
print ("")

# если выводить список с повторяющимися элементами через множества,
# эти повторяющиеся элементы не выведутся

f = ["a","g","a","r","s","a"]
print (f)
print (set(f))
print("")

# СВОЙСТВА ДЛЯ МНОЖЕСТВ

# функция len - подсчитывает количество элементов
# с помощью переменных x и y мы проверяем, есть ли число 24 и 13 в множестве g

g = {24, 57, 12.09, 790}
x = 24 
y = 13
print (x in g)
print (y in g)
print (len(g))
print ("")

# метод - isdisjoint - проверяет есть общие элементы в другом множестве, если нет, будет True, так же можно использовать оператор равенства == для проверки, соответствуют ли все элементы одной переменной или нет

j = {56, 78, 901, 34.07}
k = {1, 22.76, 63, 56}
print (a.isdisjoint (k))
print ("")

# функция update - объединяет несколько множеств вместе и выводит в рандомном порядке

l = {0, 12, 13.09}
m = {45, 90}
l.update (m)
print (l)
print ("")

# функция intersection_update указывает пересечения во множествах
# функция difference_update указывает пересечения элементов, которых нет в определенном множестве, в сравнении с другим

n = {0, 12, 13.09, 45, 67, 1}
o = {0, 90, 13.09, 1}
n.intersection_update (o)
print (n)
print ("")

# функция difference_update указывает пересечения элементов, которых нет в определенном множестве, в сравнении с другим

p = {0, 12, 13.09, 45, 67, 1}
r = {0, 90, 13.09, 1}
p.difference_update (r)
print (p)
print ("")

# функция symmetric_difference_update позволяет найти не пересекающиеся элементы во всех указанных множествах и выводит их одним множеством

s = {0, 12, 13.09, 45, 67, 1, 666, 1.24}
t = {0, 90, 13.09, 1, 457}
s.symmetric_difference_update (t)
print (s)
print ("")

# функция - remove - удаляет элементы из множества
# функция - discard -тоже удаляет элемент, но в отличие от - remove - не выдает ошибку, если такого элемента нет в множестве

u = {0, 12, 13.09, 45, 67, 1, 666, 1.24}
u.remove (666)
u.discard (111)
print (u)
print ("")

# функция - pop - удаляет первый (рандомный) элемент из множества

aa = {0, 12, 13.09}
aa.pop ()
print (aa)
print ("")

# функция - clear - очищает все множество от элементов

bb = {0, 12, 13.09}
bb.clear ()
print (bb)
print ("")





