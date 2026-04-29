# Из списка чисел от 1 до 20 составь новый список, где останутся только квадраты чётных чисел.
numbers = []
for i in range(1, 21):
    numbers.append(i)
print(numbers)
# [выражение for элемент in коллекция]
numbers2 = [i ** 2 for i in numbers if i % 2 == 0]
print(f"Результат: {numbers2}")
