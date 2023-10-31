n1 = int(input("Введите число: "))

x = n1 % 10
n2 = x
 
n1 = n1 // 10
 
while n1 > 0:
    x = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + x
 
print('Обратное число:', n2)