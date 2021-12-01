# Главный алгоритм метода прогонки
def progon(a, b):

    n = len(a)
    x = [0 for k in range(n)] # обнуление вектора решений
    
    v = [0 for i in range(n)]
    u = [0 for i in range(n)]
    
    v[0] = a[0][1] / (-a[0][0]) 
    u[0] = ( - b[0]) / (-a[0][0]) 
    
    for i in range(1, n - 1): 
        v[i] = a[i][i+1] / ( -a[i][i] - a[i][i-1]*v[i-1] )
        u[i] = ( a[i][i-1]*u[i-1] - b[i] ) / ( -a[i][i] - a[i][i-1]*v[i-1] )
    
    v[n-1] = 0
    u[n-1] = (a[n-1][n-2]*u[n-2] - b[n-1]) / (-a[n-1][n-1] - a[n-1][n-2]*v[n-2])
    
    print('Коэффициент u:')
    [print(f"v{i+1} = {round(v[i],4)}") for i in range(len(v))]
    print('\nКоэффициент v:')
    [print(f"u{i+1} = {round(u[i],4)}") for i in range(len(u))]
    
    # Обратный ход
    x[n-1] = u[n-1]
    for i in range(n-1, 0, -1):
        x[i-1] = v[i-1] * x[i] + u[i-1]
    return x    

# Чтение матрицы из файла (см. файл matrix.txt)
def get_matrix_from_file(fil = 'matrix.txt'):
	with open(fil, 'r') as f:
		n = int(f.readline())
		a = []
		for i in range(n):
			a.append(f.readline().replace('\n','').split())
		f.readline()
		b = f.readline().replace('\n','').split()
	a = [[float(j) for j in i] for i in a]
	b = [float(i) for i in b]
	return a, b, n

def main(fil = 'matrix.txt', eps = 4):
	a, b, n = get_matrix_from_file(fil)

	x = progon(a,b)
	print(f"\nОтвет: ")
	[print(f"x{i+1} = {round(x[i], eps)}") for i in range(len(x))]

	with open('ans3.txt', 'w') as f:
		f.write(str(x))
		
		print()	
	for i in range(4):
		st_out = ''
		for j in range(4):
			#print(f"{a[i]}*{x[i]} + ")
			st_out += f"{a[i][j]}*{round(x[i], eps)} + "
		st_out = st_out[:-2]
		st_out += f" = {b[i]}"
	
		print(st_out)
	

main()

