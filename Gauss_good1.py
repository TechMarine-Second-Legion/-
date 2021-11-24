def show_out(a, y, n, ou):
	print(f"Вывод №{ou}")
	for i in range(n):
		for j in range(n):
			print(f"x{j} * {a[i][j]}", end = '')
			if j < n -1:
				print(' + ', end = '')
		print(" = ", y[i])
	print()

def print_var(a, b, n):
	for i in range(n):
		for j in range(n):
			if a[i][j] == 0:
				continue
			if j == 0:
				pass
			else:
				if a[i][j-1] == 0:
					pass
				else:
					print(' + ', end = '')
			print(f"x{j} * {a[i][j]}", end = '')
			
		print(" = ", b[i])
	print()


def gauss(a, y, n):
	x = [0 for i in range(n)]
	
	eps = 0.001
	k = 0
	while k<n:
		mx = abs(a[k][k])
		index = k
		for i in range(k+1, n):
			if abs(a[i][k]) > mx:
				mx = abs(a[i][k])
				index = 1
		if mx<eps:
			print("Решению не подлежит")
			return 'No'
   
		for j in range(n):
			a[k][j], a[index][j] = a[index][j], a[k][j] 
				
		y[k], y[index] = y[index], y[k]
    
		# Нормализация уравнений
		for i in range(k, n):
			temp = a[i][k]
			if abs(temp) < eps:
				continue
			for j in range(n):
				a[i][j] /= temp
			y[i] /= temp
			if i == k: continue
			for j in range(n):
				a[i][j] -= a[k][j]
			y[i] -= y[k]
		k+=1
		show_out(a,y,n, k)

	
	# Обратный ход
	k = n-1
	while k>=0:
		x[k] = y[k]
		for i in range(k):
			y[i] = y[i] - a[i][k]* x[k]
		k-=1
	return x

def check_ans(a,b,x,eps=4, free_space = '    '):
	print("\n<Проверка>")
	n = len(a)
	print("Подстановка")
	flag = True
	for i in range(len(a)):
		s = 0
		for j in range(len(x)):
			s+=a[i][j]*x[j]
			print(f"{a[i][j]}*{round(x[j], eps)} ", end = '')
			if j < n -1:
				print(' + ', end = '')
		print(f" = {round(s,eps)}, Y{[i]} = {b[i]}, {round(s,3) == b[i]}")
		if round(s,3) != b[i]:
			flag = False
	print(f"Округление ответа производилось до {eps} знака после запятой")
	print("<\Проверка>\n")

	return flag
'''
def get_ay(fl = 'matrix.txt'):
	a = []
	with open(fl, 'r') as f:
		n = int(f.readline().replace('\n', ''))
		cnt = 0
		for line in f:
			a.append(list(line.split()))
			cnt+=1
			if cnt == n:
				break
		a = [[int(i) for i in j] for j in a]
		
		
		f.readline() # Разделение вводимых данных пустой строкой
		y = f.readline().split()
		y = [int(i) for i in y]
	return a,y,n
'''


def get_ay1(fl = 'matrix.txt'):
	a = [[4, 2,1,2],
	[1, 4, 2, 1],
	[2, 6, 1, 3],
	[2, 5, 2, 2]]
	y = [6,5,8,7]
	n=4
	return a,y,n


def main(fl = 'matrix.txt'):
	
	a,y,n = get_ay1(fl)
	
	show_out(a,y,n,0)
	
	x = gauss(a, y, n)
	
	a,y,n = get_ay1(fl)
	
	if check_ans(a,y,x):
		print("Проверенный ответ:")
		for i in range(n):
			print(f"x{i} = {x[i]}")

main()



