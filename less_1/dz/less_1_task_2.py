# 2. По введенным пользователем координатам двух точек вывести 
# уравнение прямой вида y = kx + b, проходящей через эти точки.

print('Введите координаты точки A(x1, y1):')
x1 = float(input("   x1 = "))
y1 = float(input("   y1 = "))
 
print("Введите координаты точки B(x2; y2):")
x2 = float(input("   x2 = "))
y2 = float(input("   y2 = "))
 
k = (y1 - y2) / (x1 - x2)
b = y2 - k*x2
print("Уравнение прямой вида y = kx + b, проходящей через эти точки:")
print("   y = {:.2f}*x + {:.2f}".format(k , b))
