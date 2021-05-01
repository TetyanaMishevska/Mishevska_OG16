def comparison(A, B):
    if A > B:
        print("\nУспешно")
    elif A == B:
        print("\nПочти")
    elif A < B:
        print("\nЛузер")

A = int(input("Введите число А: "))
B = int(input("Введите число В: "))

comparison(A, B)