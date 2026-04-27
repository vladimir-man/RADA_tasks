# Создай список: matrix = [[1,2,3],[4,5,6],[7,8,9]].
# Выведи элемент 5.
# Замени элемент 9 на 0
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(f"# Выведи элемент 5. \n Результат: {matrix[1][1]}")
# первый способ:
arr2 = [7, 8, 9]
arr3 = [7, 8, 0]
matrix = [[1,2,3],[4,5,6], arr3]
print(f"# Замени элемент 9 на 0/ \n Результат: {matrix}")
# второй способ
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 9:
           matrix[i][j] = 0 
for row in matrix:
    print(row)
               
print(f"# Замени элемент 9 на 0/ \n Результат: {matrix}")
# третий способ
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[(0 if x == 9 else x) for x in row] for row in matrix]
matrix = matrix2
print(f"# Замени элемент 9 на 0/ \n Результат: {matrix}")