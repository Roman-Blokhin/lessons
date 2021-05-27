# СЛОВАРИ - ассоциативные массивы

# https://www.youtube.com/watch?v=NaA2H25gxN4&list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu&index=10

# 1 способ написания
d = {"test" : 2, "hero" : "roman"} # в данном случае "test" - это ключ, 2 - это значение
print (d["test"]) #  в словарях вывод должен быть по ключу
print (d["hero"])
print ("")

# 2 способ написания
a = dict (short = "dict", longer = "dictionary")
print (type(a))
a ["short"] = 234 # таким образом можно заменить значение ключа
print (a)
print ("")

# 3 способ записи

b = dict ([("hero", 24), (56, "test")])
#  в данном случае все тоже самое, "hero" - ключ, 24 - значение
print (b)
print (type (b))
print ("")

# 4 способ записи

c = dict.fromkeys (["a", "g", "h"])
# с помощью функции .fromkeys  можно назначить ключи, если не назначать значения, они будут None - нет значений
print (c)
e = dict.fromkeys (["rt", "56", "hto", "z"], "toy")
# если после ключей задать одно значение, оно присвоится всем ключам
print (e)
print ("")

# 5 способ записи

z = {k : k ** 2 for k in range (10)} # мы ставим переменную а, начиная от нуля в степень 2 в периоде до 10 элементов
print (z)
print ("")

# Пример применения словарей

human = {"name" : {"first_name" : "roma", 'surname' : "romin", "middle_name" : "romanovich"}, "adres" : ["Moskovskaia", "h. 12", "kv. 34"], "phone" : {"mobile" : "89052345151", "home_telephone" : "84956109080"}}

print (human)
print (human ["name"]["surname"])
print (human ["adres"][2])
human ["name"] = "sem" # мы присвоили новое значение словарю
print (human ["name"])
print ("")

# метод - values - выводит все значения , без ключей
print (human.values())
print ("")

# медот keys - возвращает только ключи, без значений
print (human.keys ())
print ("")

# методоl словорей - clear - очищает словарь
human.clear ()
print (human)
print ("")






