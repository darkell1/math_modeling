a = int(input())
b = int(input())
c = int(input())

if a + b > c and b + c > a and c + a > b:
    print ("треугольник существует")
else:
    print("треугольник не существует")

if a == b == c:
    print("треугольник равносторонний")
elif a == b != c or b == c != a or c == a != b:
    print("треугольник равнобедренный") 
else:
    print("треугольник разносторонний")