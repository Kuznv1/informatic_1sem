import numpy as np # для обработки данных
import matplotlib.pyplot as plt # для построения графиков

Om = np.array([47.57, 69.8, 103.4, 124.7, 183.9])*10**(-3)

m = np.array([76.0 , 116.4, 148.5, 274.5, 341.1])
M = 0.001*m * 9.8* 0.121
T = np.array([175.0, 90.0, 60.75, 50.4, 34.17])

sigma_m = 0.02*m
Do = 3.74 * Om

sigma_Om = Do/T
sigma_M = M * np.sqrt((sigma_m/m)**2)
mu = np.mean(Om) # средее
mv = np.mean(M)
mv2 = np.mean(M**2) # средний квадрат
mu2 = np.mean(Om**2)
muv = np.mean (Om * M) # среднее от произведения
k = (muv - mu * mv) / (mv2 - mv**2)
b = mu - k * mv


'''plt.figure(figsize=(8,6), dpi=100) # размер графика
plt.ylabel("$Omega$, $рад/с * 10^-3$") # подписи к осям
plt.xlabel("$M$, $Н \dot m$")
plt.grid(True, linestyle="--") # сетка
plt.axis([0.055,0.4070 ,46,190]) # масштабы осей
x = np.array([0., 1]) # две точки аппроксимирующей прямой
plt.plot(x, k * x + b, "-r",linewidth=1) # аппроксимация
plt.errorbar(M, Om, xerr=sigma_M, yerr=sigma_Om, fmt="ok",ms=3) # точки с погрешнос
plt.legend()
plt.show()'''
I0 = 0.00733
Mtr = 0.0158*I0*2*np.pi*Om*1
print('v', k, b)
N = 5
sigma_k = np.sqrt(1/(N-2) * ( (mu2 - mu**2)/(mv2 - mv**2) - k**2 ) )
sigma_b = sigma_k * np.sqrt(mv2)
print(sigma_b, sigma_k, np.mean(sigma_M), np.mean(sigma_Om))
print(np.mean(Mtr), sigma_Om)