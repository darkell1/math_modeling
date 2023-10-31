x = int(input('Введите число 1: '))
y = int(input('Введите число 2: '))

if y == 0:
    print("Делитель равен 0, ответ 0")
else:
    print('Частное:')
    print(x / y)
    print('Остаток:')
    print(x % y)