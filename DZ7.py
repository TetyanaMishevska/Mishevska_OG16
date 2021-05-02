import random

def func(A,B,C):
    i=[]
    print([random.randint(A,B) for i in range(C)])

A=int(input("Введите нижнюю границу значений элементов списка: "))
B=int(input("Введите верхнюю границу значений элементов списка: "))
C=int(input("Введите кол-во элементов списка: "))

func(A,B,C)
