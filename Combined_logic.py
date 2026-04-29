# Из списка чисел от 1 до 15 составь новый список, где:
# если число делится на 3 → "Fizz",
# если делится на 5 → "Buzz",
# иначе само число.
# (Да, это мини‑вариант FizzBuzz через списковое включение.)
numbers = []
for i in range(1, 16):
    numbers.append(i)

numbers2 = ["Fizz" if i % 3 == 0 else ("Buzz" if i % 5 == 0 else i) for i in numbers]
print(f"Результат: {numbers2}")