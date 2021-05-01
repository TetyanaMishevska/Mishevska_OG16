def comparison(A, B, C):
    while A <= B:
        A = A + C
        print("A + C = ", A)
    print('Wow! A(', A, ') > B(', B, ")")

A = int(input("Введите число А: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))
comparison(A, B, C)