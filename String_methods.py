# Пусть есть строка "Python прост и мощен".
# Найди смещение слова "прост".
# Замени "мощен" на "сильный".
stringPy = "Python прост и мощен"
stringPy2 = "мощен"
stringPy3 = "сильный"
print(f"Слово '{stringPy2}'' найдено со смещением {stringPy.find("мощен")}.")
# ещё вариант со смещением
print(f"Слово '{stringPy2}' найдено со смещением {stringPy.index(stringPy2)}.")
# замена
print(f"Заменено в выражении:'{stringPy.replace("мощен", "сильный", 15)}' ,'{stringPy2}' на '{stringPy3}'.")