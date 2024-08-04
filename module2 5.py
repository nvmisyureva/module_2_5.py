#Домашняя работа по уроку "Функции в Python.Функция с параметром"
#Задача "Матрица воплоти":

get_matrix=[]
n = int(input("Введите количество столбцов n: "))
m = int(input("Введите количество строк m: "))
value=int(input("Введите значение: "))
matrix=[]
matrix.append([value]*n)
get_matrix.append(matrix*m)
print(get_matrix)
