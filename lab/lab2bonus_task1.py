a = int(input("первый коофицент: "))
b = int(input("второй коофицент: "))
c = int(input("третий коофицент: "))

d = b**2 - 4*a*c

if d > 0:
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)
    print (x1)
    print (x2)
elif d == 0:
    x = -b / 2*a
    print(x)
elif d < 0:
    print("Нет корней")
