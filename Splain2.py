import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np

import matplotlib.font_manager as mpt
# Импорт данных
file = 'data.txt'
a = np.loadtxt(file)
# Срез массива
x = a[:,0]  # Берем первый столбец данных
y = a[:,1]  # Берем второй столбец данных
# Выполняем сплайн-интерполяцию
tck = interpolate.splrep(x,y)
xx = np.linspace(min(x),max(x),100)
yy = interpolate.splev(xx,tck,der=0)
print(yy)

# Рисование
plt.plot(x,y,'o',xx,yy)
plt.legend(['true','Cubic-Spline'])
#plt.xlabel('')#, fontproperties=zhfont) # Обратите внимание на атрибуты шрифта позади
plt.ylabel('%')
plt.title('Заданная функция имеет вид:')#, fontproperties=zhfont)  
# сохранить изображение  
plt.savefig('out.jpg')
plt.show()

