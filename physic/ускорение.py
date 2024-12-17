import numpy as np
import math

l = 1.001
a = np.array([0.349, 0.369, 0.399, 0.429, 0.319, 0.299, 0.249, 0.279])
T = np.array([1.531, 1.536, 1.555, 1.577, 1.514, 1.512, 1.528, 1.507])

'''up = ((l**2 / 12) + a**2) * 4 * 3.1415**2
g = up / (T**2 * a)
print(g)'''

gs = []
gs = (4 * np.pi**2 * ( l**2 / 12 + a**2 ) / (a * T**2))
gm = np.mean(gs)

sigma_gm = np.std(gs) / np.sqrt(8)

print("sigma_gm = %.3f" % sigma_gm)
u = T**2 * a
v = a**2
mu = np.mean(u) # средее
mv = np.mean(v)

mv2 = np.mean(v**2) # средний квадрат
mu2 = np.mean(u**2)
muv = np.mean (u * v) # среднее от произведения
k = (muv - mu * mv) / (mv2 - mv**2)
b = mu - k * mv
print("k = ", k, ", b = ", b)

gk = (4 * np.pi**2) / k
print("g = %.3f" % gk)

N = len(v) # число точек
sigma_k = np.sqrt(1/(N-2) * ( (mu2 - mu**2)/(mv2 - mv**2) - k**2 ) )
sigma_b = sigma_k * np.sqrt(mv2)
sigma_g = sigma_k / k * gk
sigma_L = l * np.sqrt( (sigma_b / b)**2 + (sigma_g / gk)**2 )
print("sigma_k = %.3f, sigma_b = %.3f" % (sigma_k, sigma_b))
print("sigma_g = %.3f, sigma_L = %.3f" % (sigma_g, sigma_L))
Tm = np.mean(T)
print(Tm)
gb = (np.pi**2 * l**2)/(3*b)
print(gb)
sigma_gb = 9.953*0.0122
print(sigma_gb)