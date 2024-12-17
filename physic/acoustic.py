import numpy as np
import math
import matplotlib.pyplot as plt
N = 7
n1  = np.array([ 1, 2, 3, 4, 5, 6, 7])
v1 = np.array([ 3249, 6491, 9726, 13017, 16249, 19476, 23057])

n2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
v2 = np.array([4.130, 8.265, 12.381, 16.519, 20.651, 24.770, 28.892, 33.003, 39.550])

n3 = np.array([i for i in range(1, 8)])
v3 = np.array([4.235, 8.519, 12.711, 16.96, 21.109, 25.379, 27.707])
mean1 = np.mean(v1)
mean2 = np.mean(v2)
mean3 = np.mean(v3)
sigma_v = 0
sigma_v1 = np.sqrt( 1 / (N) * np.sum( (v1 - mean1)**2 ) )
sigma_v2 = np.sqrt( 1 / (9 ) * np.sum( (v2 - mean1)**2 ) )
sigma_v3 = np.sqrt( 1 / (N ) * np.sum( (v3 - mean1)**2 ) )

def mnk(v, u):
    # u = v
    # v = n
    mu = np.mean(u) # средее
    mv = np.mean(v)
    mv2 = np.mean(v**2) # средний квадрат
    mu2 = np.mean(u**2)
    muv = np.mean(u * v) # среднее от произведения
    k = (muv - mu * mv) / (mv2 - mv**2)
    b = mu - k * mv
    return k, b

k1, b1 = mnk(n1, v1)
k2, b2 = mnk(n2, v2)
k3, b3 = mnk(n3, v3)
print(k1, b1, '2:', k2, b2, '3:', k3, b3)
sigma_k1 = np.sqrt(1/(5)*((np.mean(v1**2) - (np.mean(v1))**2 ) / (np.mean(n1**2) - (np.mean(n1))**2)- (k1)**2))
sigma_k2 = np.sqrt(1/(7)*((np.mean(v2**2) - (np.mean(v2))**2 ) / (np.mean(n2**2) - (np.mean(n2))**2)- k2**2))
sigma_k3 = np.sqrt(1/(5)*((np.mean(v3**2) - (np.mean(v3))**2 ) / (np.mean(n3**2) - (np.mean(n3))**2)- k3**2))
print(sigma_k1, sigma_k2, sigma_k3)

'''plt.figure(figsize=(8,6), dpi=100) 
plt.ylabel("$f$, Гц") # подписи к осям
plt.xlabel("$n$")
plt.xlim([0, 10])
plt.grid(True, linestyle="--") # пунктирная сетка

plt.xticks(np.arange(0,12,1))
plt.axis([0,10 ,3.100,29]) # масштабы осей
x9 = np.array([0., 6.49])# две точки аппроксимирующей прямой
x = np.array([1, 2, 3, 4, 5, 6, 7])
x2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
x3 = np.array([1, 2, 3, 4, 5, 6, 7])
plt.plot(x, k1 * x, "-r",linewidth=1) # аппроксимация
plt.plot(x2, k2 * x2, "-r",linewidth=1) # аппроксимация
plt.plot(x3, k3 * x3, "-r",linewidth=1) # аппроксимация
plt.errorbar(n1, v1,xerr = 0,  yerr=sigma_v, fmt="ok",ms=3) # точки с погрешнос
plt.errorbar(n2, v2, xerr = 0, yerr=sigma_v, fmt="ok",ms=3) # точки с погрешнос
plt.errorbar(n3, v3, xerr = 0, yerr=sigma_v, fmt="ok",ms=3) # точки с погрешнос
'''
'''plt.scatter(n1,v1)
plt.scatter(n2,v2)
plt.scatter(n3,v3)

plt.plot([1, 7], [k1 + b1 * 1, k1 + b1 * 7])
plt.plot([1, 10], [k2 + b2 * 1, k2 + b2 * 9])
plt.plot([1, 7 ], [k3 + b3 * 1, k3 + b3 * 7])
'''
'''plt.legend()
plt.show()'''
#огрелов