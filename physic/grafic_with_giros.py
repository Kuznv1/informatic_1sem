import numpy as np
import matplotlib.pyplot as plt
t = np.array([0, 0.53, 2.233, 2.59, 3.24, 3.51, 4.20, 4.50, 5.25, 5.41, 6.35])
v = np.array([397,380,375, 335, 328, 320, 312, 304, 295, 290, 276])
sigma_t = 0.001
sigma_v = 17

mu = np.mean(v) # средее
mv = np.mean(t)
mv2 = np.mean(t**2) # средний квадрат
mu2 = np.mean(v**2)
muv = np.mean (v * t) # среднее от произведения
k = (muv - mu * mv) / (mv2 - mv**2)
b = mu - k * mv
plt.figure(figsize=(8,6), dpi=100) # размер графика
plt.ylabel("$V$, $Гц$") # подписи к осям
plt.xlabel("$t$, $min$")
plt.grid(True, linestyle="--") # сетка
plt.axis([0,6.5 ,270,400]) # масштабы осей
x = np.array([0., 6.35]) # две точки аппроксимирующей прямой
plt.plot(x, k * x + b, "-r",linewidth=1) # аппроксимация
plt.errorbar(t, v, xerr=sigma_t, yerr=sigma_v, fmt="ok",ms=3) # точки с погрешнос
plt.legend()
plt.show()