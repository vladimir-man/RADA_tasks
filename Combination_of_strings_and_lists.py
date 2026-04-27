# Пусть есть строка "Программирование".
# Преврати её в список символов.
# Удали все буквы "р".
# Собери строку обратно.
str = "Программирование"
# Превращаем строку в список
# 1 способ
chars = list(str)
# 2 способ
chars = [char for char in str]
# 3 способ
chars = [*str]
print(f"Было: {str}, Стало: {chars}")
# удаление 'р' 1 способ
for i in range(len(chars) - 1, -1, -1):
    if chars[i] == 'р':
        chars.pop(i)
print(f"Результат: {chars}")
# удаление 'р' второй способ
chars = list(str)
chars = [char for char in chars if char != 'р']
print(f"Результат: {chars}")
# Собираем строку обратно
str2 = "".join(chars)
print(f"Было: {str}, Стало: {str2}")
