import Gpoint as gaus

sum_sign = '∑'

print("Уравнение линейной регрессии имеет вид: y = bx + a")
print("Находим параметры уравнения методом наименьших квадратов (МНК)", end = '\n\n')
print("Система уравнений МНК:")
print(f"an + b{sum_sign}x = {sum_sign}y")
print(f"a{sum_sign}x + b{sum_sign}x^2 = {sum_sign}y*x", end = '\n\n')

n = 4
x = [-1,  2,  3,   4]
y = [-1, -7, -9, -11]


print("Введёные координаты точек:")
print(f"x = {x}")
print(f"y = {y}", end= '\n\n')

x2 = [i**2 for i in x]
y2 = [i**2 for i in y]
xy = [x[i] * y[i] for i in range(n)]



print(f"Квадраты точек:\nx^2 = {x2}")
print(f"y^2 = {y2}")
print(f"xy = {xy}", end = '\n\n')

print("Система для введённых данных имеет вид:")
print(f"{n}a + {sum(x)}b = {sum(y)}")
print(f"{sum(x)}a + {sum(x2)}b = {sum(xy)}")
print()

print(f"Решенеи матрицы через Гаусса (ЛР №2)")
print("<Gauss>")
x = gaus.gauss([[n, sum(x)],[sum(x), sum(x2)]],[sum(y), sum(xy)],2)
a,b = x
print(f"x = {x}")
print("<\Gauss>")

print(f"a = {a}, b = {b}\n")


print(f"Готовое уравнение регрессии: \ny = {b}*x {a}")

