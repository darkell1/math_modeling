n = int(input())
while n > 1:
    x = 2
    y = 0
    while True:
        if n % x == 0:
            n = n // x
            print(x, end =" ")
            y = 1
            break
        else:
            x += 1
    if y == 1:
        continue
print()