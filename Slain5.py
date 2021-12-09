#!/usr/bin/env python3

from scipy.interpolate import CubicSpline

def input_from_file(fl = "points.txt"):
    try:
        with open(fl, 'r') as f:
            n = int(f.readline().replace('\n','')) # Первая строка - кол-во точек
            x = []
            y = []
            for i in range(n):
                x1, y1 = tuple(f.readline().replace('\n','').split())
                x.append(x1)
                y.append(y1)

        print(f"Количество точек: {n}")
        print(f"Координаты х: {x}")
        print(f"Координаты y: {y}", end = '\n\n')
        return x,y,n
    except:
        print(f"Файл '{fl}' не найден или содержимое не корректно")
        pass
        return 0,0,0

def main(eps = 3):
    x, y, n = input_from_file()

    cs = CubicSpline(x,y,bc_type='natural')
    cs.c
    a = []
    b = []
    c = []
    d = []

    for i in range(5):
        a.append(cs.c.item(3,i))
        b.append(cs.c.item(2,i))
        c.append(cs.c.item(1,i))
        d.append(cs.c.item(0,i))

    for i in range(5):
        print(f'S{i}({x[i]}<=x<={x[i+1]}) = ', round(a[i], eps), ' + ', round(b[i],eps), '(x-0) + ', round(c[i],eps) , '(x-0)^2  + ', round(d[i],eps), '(x-0)^3')

main()


# So we can calculate S(1.25) by using equation S1(1< x<=2)
#print('S(1.25) = ', a1 + b1*0.25 + c1*(0.25**2) + d1*(0.25**3))

# Cubic spline interpolation calculus example
#  https://www.youtube.com/watch?v=gT7F3TWihvk
