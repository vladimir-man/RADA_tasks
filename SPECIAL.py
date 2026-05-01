# Есть список слов:
# words = ["python", "java", "ruby", "c", "go", "rust"]
# Построй новый список, где:
# если индекс слова чётный → "EVEN-<индекс>-<слово>"
# если индекс нечётный → "ODD-<индекс>-<слово в верхнем регистре>"
# НО если слово начинается с буквы "r" → независимо от индекса заменить его на "SPECIAL"
# Подсказка: придётся комбинировать enumerate() и дополнительное условие внутри тернарного оператора
words = ["python", "java", "ruby", "c", "go", "rust"]
words_new = ["SPECIAL" if word.startswith("r") else(f"EVEN-{i}-{word}" if i % 2 == 0 else f"ODD-{i}-{word.upper()}") for i, word in enumerate(words)]
print(f"Результат: {words_new}")