import random

def func(A,B,C):
    i1 = [random.randint(A,B) for i1 in range(C)]
    print(i1)
    i2 = [random.randint(A, B) for i2 in range(C)]
    print(i2)
    if i1 == i2:
        print('Списки одинаковые)')
    else:
        result = list(set(i1) ^ set(i2))
        print("Уникальные числа:", result)

A=int(input("Введите нижнюю границу значений элементов списка: "))
B=int(input("Введите верхнюю границу значений элементов списка: "))
C=int(input("Введите кол-во элементов списка: "))

func(A,B,C)





