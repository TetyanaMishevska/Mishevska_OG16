def tadam (A):
    sum = 0
    while A > 0:
        digit = A % 10
        sum = sum + digit
        A = A // 10
    print('Сумма:',sum)

A = int(input('Введите число '))

tadam (A)
