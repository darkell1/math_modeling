x = int(input())

x1 = x // 1000
x2 = x // 100
x3 = x // 10
x4 = x // 1

xx2 = x2 * 10
xx3 = x3 * 100
xx4 = x4 * 1000

x0 = x1 + xx2 + xx3 + xx4

print(x0)