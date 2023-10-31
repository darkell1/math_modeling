b1 = int(input('нулевое число: '))
n = int(input('кол во членов: '))
q = int(input('знаменатель: '))

b0 = b1

for i in range (0, n, 1):
    b2 = b0 * q
    print(b2)
    b0 = b2


    
