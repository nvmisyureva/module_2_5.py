#Домашняя работа по уроку "Функции в Python.Функция с параметром"
#Задача "Матрица воплоти":

def get_matrix(n,m,value):
    a=[value]*n
    matrix=[a]*m
    return matrix

n = int(input("Введите количество столбцов n: "))
m = int(input("Введите количество строк m: "))
value = int(input("Введите значение: "))
matrix=get_matrix(n,m,value)
print(matrix)
