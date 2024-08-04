# Матрица. Вариант2
n = int(input("Введите количество строк n:"))
m = int(input("Введите количество столбцов m:"))

get_matrix = []
print("Введите числа матрицы попорядку в строках:")

for i in range(n):
    matrix = []
    for j in range(m):
        matrix.append(int(input()))
    get_matrix.append(matrix)
for i in range(n):
   for j in range(m):
      print(get_matrix[i][j], end = " ")
   print()
