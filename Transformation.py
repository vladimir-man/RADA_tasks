# Есть список слов: ["python", "java", "ruby", "c"]. Построй новый список, где каждое
# слово начинается с заглавной буквы, но если длина слова меньше 3 символов — замени его
# на "*".
from annotated_types import Len


numbers = ["python", "java", "ruby", "c"]
numbers2 = ['*' if len(i) < 3 else i and i.capitalize() for i in numbers]
print(f"Результат: {numbers2}")