# Есть список слов:
# words = ["python", "java", "ruby", "c", "go", "rust"]
# Построй новый список, где:
# если индекс слова чётный → строка "EVEN-<индекс>-<слово>"
# если индекс нечётный → строка "ODD-<индекс>-<слово в верхнем регистре>"
# Подсказка: нужно использовать enumerate() внутри list comprehension, чтобы получить и индекс, и значение.
words = ["python", "java", "ruby", "c", "go", "rust"]
words_new = [f"EVEN {i} {word}" if i % 2 == 0 else f"ODD {i} {word.upper()}" for i, word in enumerate(words) ]
print(f"Результат: {words_new}")