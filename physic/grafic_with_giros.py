import numpy as np
import matplotlib.pyplot as plt
t = np.array([1/(333*8.31), 1/(353*8.31)])
v = np.array([0.838*40*10**(-5), 0.735*40*10**(-5)])
sigma_t = 0.001
sigma_v = 17

mu = np.mean(v) # средее
mv = np.mean(t)
mv2 = np.mean(t**2) # средний квадрат
mu2 = np.mean(v**2)
muv = np.mean (v * t) # среднее от произведения
k = (muv - mu * mv) / (mv2 - mv**2)
b = mu - k * mv
'''plt.figure(figsize=(8,6), dpi=100) # размер графика
plt.ylabel("$V$, $Гц$") # подписи к осям
plt.xlabel("$t$, $min$")
plt.grid(True, linestyle="--") # сетка
plt.axis([0,6.5 ,270,400]) # масштабы осей
x = np.array([0., 6.35]) # две точки аппроксимирующей прямой
plt.plot(x, k * x + b, "-r",linewidth=1) # аппроксимация
plt.errorbar(t, v, xerr=sigma_t, yerr=sigma_v, fmt="ok",ms=3) # точки с погрешнос
plt.legend()
plt.show()'''
print(k, b)