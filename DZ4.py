def math(A , B):
    return A + B, A - B, A * B, A // B

A = int(input("Введите число А: "))
B = int(input("Введите число В: "))

if( B == 0 ):
    print(f"({A + B},{A - B},{A * B},Ошибка:деление на ноль)")
else:
    math(A, B)
    print(math(A, B))
